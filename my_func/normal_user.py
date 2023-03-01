import streamlit as st


def pdf_file():
    pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])