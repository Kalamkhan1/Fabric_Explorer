from state_graph import chat_with_human_graph
import streamlit as st
from langchain_core.messages.ai import AIMessage
# Start the conversation
state = chat_with_human_graph.invoke({"messages": []})


# Create a Streamlit interface
st.title("Fabrica Chatbot - Fashion Fabric Assistant")

# Show the conversation history
for message in state["messages"]:
    if isinstance(message, AIMessage):
        st.write(f"**Fabrica**: {message.content}")
    else:
        st.write(f"**User**: {message[1]}")

# Handle user input and chat flow
if st.text_input("Ask Fabrica:"):
    state = chat_with_human_graph.invoke(state)
    # Re-render the chat interface with the updated state
    for message in state["messages"]:
        if isinstance(message, AIMessage):
            st.write(f"**Fabrica**: {message.content}")
        else:
            st.write(f"**User**: {message[1]}")
