import streamlit as st
import requests
from io import BytesIO
import google.generativeai as genai
from IPython.display import HTML, Markdown, display
from google.api_core import retry



def app():
    GOOGLE_API_KEY = "AIzaSyCCGGL1-Pv9YXvJrb2fuolNvgHSDryW3eU"
    genai.configure(api_key=GOOGLE_API_KEY)
    flash = genai.GenerativeModel('gemini-1.5-flash')

    few_shot_prompt = """
You are Fabrica, a knowledgeable and friendly virtual assistant created to guide fashion design students in their fabric-related journey. Your primary role is to provide in-depth information and insights about fabrics, including their types, properties, textures, durability, and best use cases for fashion design. You are an expert in fabrics and their applications in the world of fashion design, and you assist students in making informed decisions based on their project needs.

Your guidance includes answering questions about various fabric types, such as natural fibers, synthetic fibers, blends, and other fabric categories. You should explain their qualities, textures, and ideal uses, helping students choose the best fabric for different fashion projects.

You should also provide advice on fabric combinations, how to pair fabrics for different styles, and explain the role of each fabric in creating specific designs. When asked about trends, you will provide up-to-date information on current fabric styles, sustainability, and how fabrics are evolving in the fashion world.

Your responses should be clear, well-explained, and helpful, with an emphasis on providing valuable insights for fashion design students. Stay on topic, focusing on fabric-related queries. Be patient, professional, and polite.

If you don't know the answer to a question, let the user know you're not sure and suggest alternative resources. Always aim to help them further their understanding of fabrics and their applications in fashion design.
    
"""

    
  
    # Set title and introduction for the app
    st.title("Fabrica")
    st.markdown("""
    Hi! I'm **Fabrica**! Ask me anything about fabrics, and I'll help you out. Whether you're curious about fabric types, their properties, how to pair them, or even visualizing the latest clothing trends, I am here to assist you! Let’s explore the world of fabrics together!
    """)
    
    # Create two tabs: one for chat and one for visualizing fabric info
    chat_tab, visualize_tab = st.tabs(["Chat", "Visualize"])

    # Initialize the session state for storing conversation history
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""  # Initialize input value

    # Chatbot section (within the "Chat" tab)
    with chat_tab:
        st.markdown("#### Chat with Fabrica")

        # Function to handle user inputs and generate responses
        def get_bot_response(user_input):
            # Simple example: This can be expanded to include more sophisticated responses
            retry_policy = {
    "retry": retry.Retry(predicate=retry.if_transient_error, initial=10, multiplier=1.5, timeout=300)
}
            response = flash.generate_content([few_shot_prompt, user_input],request_options=retry_policy)
            print(response.text)

            # Generate a response based on the user input
            return response.text

        # Display the chat history (conversation above the text input)
        chat_area = st.empty()  # Placeholder for dynamic chat display

        with chat_area.container():
            for message in st.session_state.conversation:
                if message[0] == "You":
                    st.markdown(f"**You**: {message[1]}")
                else:
                    st.markdown(f"**Bot**: {message[1]}")

        # Create a new row to hold the input field
        st.markdown("<hr>", unsafe_allow_html=True)  # Divider between conversation and text input

        # User input section at the bottom of the page
        user_input = st.text_input("Ask a question about fabrics:", "", key="user_input")

        if user_input:
            # Add user input to the conversation history
            st.session_state.conversation.append(("You", user_input))

            # Get the chatbot's response
            bot_response = get_bot_response(user_input)

            # Add bot response to the conversation history
            st.session_state.conversation.append(("Bot", bot_response))

            # Update chat display after response
            chat_area.empty()  # Clear the chat area and re-render with the new message

            # Re-render the conversation
            with chat_area.container():
                for message in st.session_state.conversation:
                    if message[0] == "You":
                        st.markdown(f"**You**: {message[1]}")
                    else:
                        st.markdown(f"**Bot**: {message[1]}")

        # Option to reset the conversation history
        if st.button("Start a new conversation"):
            st.session_state.conversation = []

    # Visualize section (within the "Visualize" tab)
    with visualize_tab:
        st.subheader("Visualize With Fabrica")

        # Take prompt input from user
        prompt = st.text_input("Enter a prompt to visualize fabric (e.g., 'blue silk fabric with floral design'):")

        if prompt:
            # API URL (Replace with your actual API endpoint)
            api_url = "https://244f-34-125-86-239.ngrok-free.app/generate"  # Replace with your actual ngrok URL or API endpoint
            prompt = prompt.replace(" ", "+")
            
            # Send prompt to API (e.g., a model like Stable Diffusion or any other API)
            response = requests.get(api_url, params={"prompt": prompt})
            print(response)

            if response.status_code == 200:
                # Get the image from the API response and display it
                image_data = response.content  # This assumes the API sends the image as raw data
                image = BytesIO(image_data)  # Convert the image data to an image stream
                st.image(image, caption="Generated Fabric Image", use_column_width=True)
            else:
                st.error("Error generating image. Please try again.")

# To run the app as a Streamlit page, call app() in main.py
if __name__ == "__main__":
    app()
