from langgraph.graph import StateGraph, START
from fabricaBot import chatbot_with_welcome_msg, human_node, maybe_exit_human_node,OrderState

# Set up the initial graph based on our state definition.
graph_builder = StateGraph(OrderState)

graph_builder.add_node("chatbot", chatbot_with_welcome_msg)
graph_builder.add_node("human", human_node)

# Start with the chatbot again.
graph_builder.add_edge(START, "chatbot")
print("it worked")
# The chatbot will always go to the human next.
graph_builder.add_edge("chatbot", "human")
graph_builder.add_conditional_edges("human", maybe_exit_human_node)
chat_with_human_graph = graph_builder.compile()