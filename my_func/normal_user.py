import streamlit as st
from my_func import show_pdf
import os

def pdf_file():
    try:
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        if pdf_file is not None:
            if os.path.exists("./resume_data") == False:
                os.mkdir("./resume_data")
            pdf_path="./resume_data"
            
            with open(pdf_path+"/"+pdf_file.name,'wb') as f:
                f.write(pdf_file.getvalue())
            pdf_file_path=pdf_path+"/"+pdf_file.name
            show_pdf.display_pdf(pdf_file_path)
     
    except Exception as e:
        st.write(str(e))