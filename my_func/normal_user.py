import streamlit as st


def pdf_file():
    try:
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
    except Exception as e:
        st.write(str(e))