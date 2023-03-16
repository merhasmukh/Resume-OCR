import streamlit as st 
from src.components import normal_user,show_pdf,date_and_time
from src.components import pdf_to_text,pdf_to_images,name_extract,email_extract,num_extract
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
            pdf_file_path,pdf_file_name=normal_user.pdf_file()
            # pdf_to_images.pdf_2_image(pdf_file_path,pdf_file_name)
            all_text=pdf_to_text.PdfToText.pdf_miner(pdf_file_path)
            if all_text is not None:
                # st.write(all_data)
                name=name_extract.extract_name(all_text)
                email=email_extract.extract_email(all_text)
                mobile_no=num_extract.extract_number(all_text)
                st.write({'Name': name })

                st.write({"Email":email})
                st.write({"Mobile No":mobile_no})
                st.write({"Date":date_and_time.getDate()})
                st.write({"Time":date_and_time.getTime()})
        elif choice=="Admin":
            logging.info(" Admin Selected..!!")
           
            
        else:
            st.write("Select Your Choice")
    except Exception as e:
        st.write(str(e))

main()