import streamlit as st
import Beginner
import Intermediate
import Advanced

def app():
    # Title and Introduction
    st.title("Learning Paths")
    st.markdown("""
    Choose a learning path based on your current knowledge of fabrics.
    You can select a level (Beginner, Intermediate, or Advanced) or take a quiz to help decide.
    """)

    # Styling for buttons (using custom CSS)
    st.markdown("""
        <style>
        .big-button {
            width: 300px;
            height: 60px;
            font-size: 20px;
            margin: 20px;
            display: inline-block;
        }
        .quiz-button {
            width: 300px;
            height: 60px;
            font-size: 20px;
            margin: 20px;
            display: block;
            background-color: #ff7f50;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Buttons for each learning path
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Beginner", key="beginner", help="Start with the basics of fabrics.", use_container_width=True):
            st.subheader("Beginner Learning Path")
            st.markdown("""Start with the basics! You'll learn about the different fabric types, their properties, 
            and how to identify them. Ideal for those new to fabric exploration.""")
            #Beginner.app()


    with col2:
        if st.button("Intermediate", key="intermediate", help="Take your fabric knowledge to the next level.", use_container_width=True):
            st.subheader("Intermediate Learning Path")
            st.markdown("""Dive deeper into fabric characteristics, understanding how to choose fabrics for different projects, 
            and more advanced textile concepts.""")
            #Intermediate.app()

    with col3:
        if st.button("Advanced", key="advanced", help="Master the art of fabric science and design.", use_container_width=True):
            st.subheader("Advanced Learning Path")
            st.markdown("""Master the art of fabric selection! Explore complex fabric science, sustainable fabrics, and advanced techniques for designing with fabrics.""")
            #Advanced.app()

    # Quiz Button
    st.markdown("<hr>", unsafe_allow_html=True)  # Divider between buttons and quiz
    if st.button("Can't make a choice? Take this quiz", key="quiz", help="Take a quiz to help you choose a path.", use_container_width=True):
        st.session_state.quiz_shown = True  # Show the quiz when the button is clicked

    # Show the quiz if it's triggered
    if st.session_state.get('quiz_shown', False):
        take_quiz()

def take_quiz():
    # Quiz to determine learning path
    st.markdown("### Fabric Knowledge Quiz")

    # Sample quiz questions
    question_1 = st.radio("1. What is the most common fabric used in summer clothing?", ["Cotton", "Wool", "Silk", "Denim"], key="q1")
    question_2 = st.radio("2. What fiber is typically used to make denim?", ["Linen", "Polyester", "Cotton", "Silk"], key="q2")
    question_3 = st.radio("3. Which fabric is known for its luxurious feel?", ["Cotton", "Silk", "Linen", "Polyester"], key="q3")

    if question_1 and question_2 and question_3:
        score = 0
        if question_1 == "Cotton":
            score += 1
        if question_2 == "Cotton":
            score += 1
        if question_3 == "Silk":
            score += 1

        # Based on score, assign a learning path
        if score == 0:
            st.warning("It seems like you're a beginner! We recommend starting with the **Beginner** learning path.")
        elif score == 1:
            st.warning("You're in the **Intermediate** category! Keep exploring more advanced topics.")
        elif score == 2 or score == 3:
            st.success("You're an expert! We recommend the **Advanced** learning path.")
    else:
        st.warning("Please answer all the questions to get your result.")

    
# To run the app as a Streamlit page, call app() in main.py
if __name__ == "__main__":
    app()
