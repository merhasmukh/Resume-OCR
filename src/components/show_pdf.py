
import base64
import streamlit as st
from src.logger import logging

def display_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
        logging.info(" Pdf Displayed...")
        
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.write(str(e))