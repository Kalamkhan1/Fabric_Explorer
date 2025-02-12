from langchain_core.messages.ai import AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Annotated, Literal, TypedDict
from embeddings import db
# Initialize the LLM


class OrderState(TypedDict):
    """State representing the customer's order conversation."""

    # The chat conversation. This preserves the conversation history
    # between nodes. The `add_messages` annotation indicates to LangGraph
    # that state is updated by appending returned messages, not replacing
    # them.
    messages: Annotated[list, add_messages]

    # The customer's in-progress order.
    order: list[str]

    # Flag indicating that the order is placed and completed.
    finished: bool

FABRICA_SYSINT = (
    "system",  # 'system' indicates the message is a system instruction.
    "You are Fabrica, a knowledgeable and friendly virtual assistant created to guide fashion design students in their fabric-related journey. Your primary role is to provide in-depth information and insights about fabrics, including their types, properties, textures, durability, and best use cases for fashion design. You are an expert in fabrics and their applications in the world of fashion design, and you assist students in making informed decisions based on their project needs. "
    "As Fabrica, you will answer questions about various fabric types, such as natural fibers, synthetic fibers, blends, and other fabric categories, along with detailed descriptions of their qualities. You will also provide guidance on choosing the right fabric based on the specific project requirements, be it for casual wear, formal attire, eco-friendly products, or other fashion design needs. "
    "Additionally, you will offer valuable advice on fabric combinations, the right textures, color pairings, and how different fabrics work together to achieve the desired design. You will keep track of the latest trends in fabrics and fashion, providing up-to-date advice on what fabrics are in vogue, their role in contemporary fashion, and how they can enhance design creativity. "
    "Your guidance will not be limited to fabric properties alone; you will also assist students with suggestions on fabric care, maintenance tips, and sustainability aspects, ensuring that fashion design students have a holistic understanding of fabric selection. "
    "You should always aim to offer clear, well-explained, and helpful responses. Whenever appropriate, provide additional resources, tips, or further reading materials to enhance the learning experience of the students. "
    "You must remain focused on fabric and fashion design-related queries. If the conversation veers off-topic, gently steer the user back to the fabric-related subject matter. Always be polite, patient, and professional, and when in doubt, ask clarifying questions to ensure you provide the best possible guidance. "
    "Your mission is to empower fashion design students with the knowledge and confidence they need to make informed choices when it comes to selecting fabrics for their design projects, while promoting creativity and sustainability in fashion."
)

# This is the message with which the system opens the conversation.
WELCOME_MSG = " Welcome to Fabrica, your virtual assistant for all things fabric! Type `q` to quit. How may I serve you today?"

try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
except Exception as e:
    print(f"Error initializing model: {e}")



def chatbot(state: OrderState) -> OrderState:
    """The chatbot itself. A simple wrapper around the model's own chat interface."""
    message_history = [FABRICA_SYSINT] + state["messages"]
    return {"messages": [llm.invoke(message_history)]}


def human_node(state: OrderState) -> OrderState:
    """Display the last model message to the user, and receive the user's input."""
    last_msg = state["messages"][-1]
    print("Model:", last_msg.content)

    query = input("User: ")
    
    result = db.query(query_texts=[query], n_results=1)
    [[passage]] = result["documents"]
    passage_oneline = passage.replace("\n", " ")
    query_oneline = query.replace("\n", " ")




    # This prompt is where you can specify any guidance on tone, or what topics the model should stick to, or avoid.
    prompt = f"""
    PASSAGE: {passage_oneline}
    QUESTION: {query_oneline}
    """

    # If it looks like the user is trying to quit, flag the conversation
    # as over.
    if query in {"q", "quit", "exit", "goodbye"}:
        state["finished"] = True

    return state | {"messages": [("user", query)]}


def maybe_exit_human_node(state: OrderState) -> Literal["chatbot", "__end__"]:
    """Route to the chatbot, unless it looks like the user is exiting."""
    if state.get("finished", False):
        return END
    else:
        return "chatbot"


def chatbot_with_welcome_msg(state: OrderState) -> OrderState:
    """The chatbot itself. A wrapper around the model's own chat interface."""

    if state["messages"]:
        # If there are messages, continue the conversation with the Gemini model.
        new_output = llm.invoke([FABRICA_SYSINT] + state["messages"])
    else:
        # If there are no messages, start with the welcome message.
        new_output = AIMessage(content=WELCOME_MSG)

    return state | {"messages": [new_output]}
