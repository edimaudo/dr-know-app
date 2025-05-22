import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👋",
)

st.title("Dr Know")
st.header("About")

st.markdown(
    """
    Human beings are wonderful but we can get run down by aches, pains and sickness.    
    Dr Know provides a high level health diagnostic tool that people can use in the convenience of their homes to understand health issues they may have.
    It is not a replacement for a doctor but a conversation starter.  
    It is built using [streamlit](https://streamlit.io/cloud) and [Gemini](https://aistudio.google.com/).
    """
)