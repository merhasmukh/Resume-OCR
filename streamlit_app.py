import streamlit as st 
from src.components import normal_user,show_pdf
from src.components import pdf_to_text
from src.logger import logging

st.set_page_config(
    page_title="Resume OCR",
    page_icon=""
)


def main():
    try:
        st.title("Resume OCR")

        st.sidebar.markdown("## Choose User")
        activities = ["Normal User", "Admin"]
        choice = st.sidebar.selectbox("Choose among the given options:", activities)
        if choice=='Normal User':
            logging.info("Normal User Selected..!!")
            pdf_file_name=normal_user.pdf_file()
            all_data=pdf_to_text.PdfToText.pdf_miner(pdf_file_name)
            if all_data is not None:
                st.write(all_data)
            
        elif choice=="Admin":
            logging.info(" Admin Selected..!!")
            pass
            
        else:
            st.write("Select Your Choice")
    except Exception as e:
        st.write(str(e))

main()