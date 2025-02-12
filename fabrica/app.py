import chromadb
from chromadb import Embeddings
from google.api_core import retry
from typing import Annotated
from typing_extensions import TypedDict
import os
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.embeddings.base import Embeddings
from typing import List, Literal
from langchain_core.messages.ai import AIMessage
import streamlit as st
from langchain.schema import HumanMessage, AIMessage

# Set up environment and initial configurations
GOOGLE_API_KEY = ""
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize documents and database
fashion = "yuio"
asia_doc = "dfgh"
africa_doc = "gjctj"
europe_doc = "asdfgh"
fashion_trends = "qwert"
extra_fashion = "cvbn"
north_america_doc = "jkl"
documents = [fashion, asia_doc, africa_doc, europe_doc, north_america_doc, extra_fashion, fashion_trends]

# Define embedding function
class GeminiEmbeddingFunction(Embeddings):
    def __init__(self, document_mode=True):
        self.document_mode = document_mode
        self.embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return self.embedding_model.embed_documents(documents)

    def embed_query(self, query: str) -> List[float]:
        return self.embedding_model.embed_query(query)

    def __call__(self, input: List[str]) -> List[List[float]]:
        if self.document_mode:
            return self.embed_documents(input)
        else:
            return [self.embed_query(q) for q in input]

# Set up Chroma client
DB_NAME = "Fabrics3"
embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True
chroma_client = chromadb.HttpClient(host="localhost", port=8000, tenant="default_tenant")
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

if len(db.get()["documents"]) < len(documents):
    ids = [str(i) for i in range(len(documents))]
    embeddings = embed_fn(documents)
    db.add(documents=documents, embeddings=embeddings, ids=ids)

# Define state
class OrderState(TypedDict):
    messages: Annotated[list, add_messages]
    order: list[str]
    finished: bool

# System and welcome messages
FABRICA_SYSINT = ("system", "You are Fabrica, a knowledgeable and friendly virtual assistant...")
WELCOME_MSG = "Welcome to Fabrica, your virtual assistant for all things fabric! Type `q` to quit. How may I serve you today?"

# Initialize the model
try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
except Exception as e:
    print(f"Error initializing model: {e}")

# Define human node logic
def human_node(state: OrderState) -> OrderState:
    if "input_key" not in st.session_state:
        st.session_state["input_key"] = 0

    if len(state["messages"]) == 0:
        input_key = f"input_{st.session_state['input_key']}"
        query = st.text_input("Your message:", key=input_key)

        if query.strip():
            result = db.query(query_texts=[query], n_results=1)
            [[passage]] = result["documents"]
            passage_oneline = passage.replace("\n", " ")
            query_oneline = query.replace("\n", " ")

            prompt = f"PASSAGE: {passage_oneline}\nQUESTION: {query_oneline}"
            state["messages"].append(HumanMessage(content=prompt))

            if query in {"q", "quit", "exit", "goodbye"}:
                state["finished"] = True

    if state["messages"]:
        if isinstance(state["messages"][-1], AIMessage):
            last_msg = state["messages"][-1]
            st.write(last_msg.content)

            input_key = f"input_{st.session_state['input_key']}"
            query = st.text_input("Your message:", key=input_key)

            if query.strip():
                result = db.query(query_texts=[query], n_results=1)
                [[passage]] = result["documents"]
                passage_oneline = passage.replace("\n", " ")
                query_oneline = query.replace("\n", " ")

                prompt = f"PASSAGE: {passage_oneline}\nQUESTION: {query_oneline}"
                state["messages"].append(HumanMessage(content=prompt))

                if query in {"q", "quit", "exit", "goodbye"}:
                    state["finished"] = True

    st.session_state["input_key"] += 1
    return state

# Function to manage state transitions
def maybe_continue_human(state: OrderState) -> Literal["chatbot", "__end__"]:
    if state.get("finished", False):
        return "__end__"

    if len(state.get("messages", [])) > 0:
        last_message = state["messages"][-1]
        if isinstance(last_message, HumanMessage):
            return "chatbot"

    return "human"

# Define the chatbot response
def chatbot_with_welcome_msg(state: OrderState) -> OrderState:
    if state["messages"]:
        new_output = llm.invoke([FABRICA_SYSINT] + state["messages"])
    else:
        new_output = AIMessage(content=WELCOME_MSG)
    return state | {"messages": [new_output]}

# Set up the graph
graph_builder = StateGraph(OrderState)

# Add nodes and edges to the graph
graph_builder.add_node("chatbot", chatbot_with_welcome_msg)
graph_builder.add_node("human", human_node)
graph_builder.add_edge(START, "human")
graph_builder.add_edge("chatbot", "human")
graph_builder.add_conditional_edges("human", maybe_continue_human)

# Compile and initialize the graph
chat_with_human_graph = graph_builder.compile()

st.title("Fabrica: Virtual Fabric Assistant")
state = chat_with_human_graph.invoke({"messages": []})
