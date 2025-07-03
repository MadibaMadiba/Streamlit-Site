import streamlit as st

st.title("Home")
st.set_page_config(
    layout="centered",
    page_title="Madiba Nyadwe's microsite",
    page_icon=":wilted_flower:",
    # initial_sidebar_state="expanded"
)

dummy1, actual, dummy2 = st.columns(3)
with actual:
    st.image("assets/profile.jpg")
    st.write("Python developer | Data Analyst | Data Scientist | Green cat (true)")

st.subheader("Skills")
st.markdown("""
- :wilted_flower:
- other things will go here later
""")