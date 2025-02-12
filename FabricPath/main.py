import streamlit as st
import fabricExplorer
import LearningPaths
import Fabrica
import Beginner
import Intermediate
import Advanced

# App title and layout
st.set_page_config(page_title="FabricPath", layout="wide")

# Sidebar Navbar
def navbar():
    with st.sidebar:
        st.markdown("""
    <h1 style="font-size: 50px; font-weight: bold; text-decoration: underline; text-align: center;">
        FabricPath
    </h1>
        """, unsafe_allow_html=True)
        page = st.radio("",["Home", "Fabric Explorer", "Learning Paths", "Beginner Path", "Intermediate Path", "Advanced Path", "Fabrica"])
        st.markdown("---")
        st.write("Explore the fascinating world of fabrics and enhance your learning!")
        return page

# Main Home Page Content
def home_page():
    st.title("Welcome to FabricPath!")
    st.markdown("""
    ### Features of FabricPath
    1. **Fabric Explorer**: 
        - An interactive fabric search and comparison mechanism.
        - Connects to a powerful **Node.js** backend for dynamic data exploration.

    2. **Learning Paths**:
        - A tailored learning system based on your quiz performance.
        - Personalized recommendations for mastering fabric knowledge.

    3. **Fabrica : Your Tailored Textile Assistant**:
        - Your personal fabric assistant.
        - Offers suggestions on fabric combinations and preferences.

    ---
    **Start your journey today and discover the art of fabric selection and design!**
    """)

# App Routing
def main():
    page = navbar()

    if page == "Home":
        home_page()
    elif page == "Fabric Explorer":
        fabricExplorer.app()
    elif page == "Learning Paths":
        LearningPaths.app()
    elif page ==  "Beginner Path":
        Beginner.app()
    elif page == "Intermediate Path":
        Intermediate.app()
    elif page ==  "Advanced Path":
        Advanced.app()
    elif page == "Fabrica":
        Fabrica.app()

if __name__ == "__main__":
    main()