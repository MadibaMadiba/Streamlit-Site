import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="My Projects",
    page_icon=":boom:"
    # initial_sidebar_state="expanded"
)
st.header("My Projects")
st.subheader("Wuthering Waves Calculator")
st.caption("Personal - Unfinished")
st.markdown("""
- A tool to dynamically calculate the damage dealt by characters in Wuthering Waves with actions input by the user
""")
# st.image("placeholder.jpg")

st.subheader("Some other")
st.caption("Work - Ongoing")