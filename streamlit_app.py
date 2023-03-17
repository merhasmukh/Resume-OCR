import streamlit as st 
from src.utils import getDate,getTime,create_txt_file,delete_file,read_txt_file
from src.components import normal_user
from src.components import pdf_to_text,pdf_to_images,name_extract,email_extract,num_extract
from src.components import easy_ocr
from src.logger import logging
import os
st.set_page_config(
    page_title="Resume OCR",
    page_icon=""
)


def main():
    try:
        st.title("Resume OCR")

        st.sidebar.markdown("## Choose User")
        activities = ["Normal User","EasyOCR", "Admin"]
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
                st.write({"Date":getDate()})
                st.write({"Time":getTime()})
            else:
                st.write("Select Your file")


        elif choice=='EasyOCR':
            logging.info("EasyOCR Selected..!!")
            all_text_list=[]
            pdf_file_path,pdf_file_name=normal_user.pdf_file()
            image_dir=pdf_to_images.pdf_2_image(pdf_file_path,pdf_file_name)

            print(image_dir)
            for i in range(len(os.listdir(image_dir))):
                print("img>>>",i)
                file_name=pdf_file_name.replace(".pdf","")
                image_path=os.path.join("resume_data","pdf_to_image",file_name,"page"+str(i)+".jpg")
                print("image path",image_path)
                text_list=easy_ocr.EasyOCR.extract_all_text(image_path)
                delete_file(image_path)

                text_file_path=os.path.join("resume_data","pdf_to_image",file_name+".txt")
                print("text_file_path",text_file_path)
                create_txt_file(text_file_path,text=text_list)

                # all_text_list=all_text_list.append(text_list)
                
                # break
            all_text_list=read_txt_file(text_file_path)
            name=easy_ocr.EasyOCR.get_name(all_text_list)
            email=easy_ocr.EasyOCR.get_mail(all_text_list)
            number=easy_ocr.EasyOCR.get_number(all_text_list)

            delete_file(text_file_path)
            st.write({"name":name,"email":email,"number":number})


        elif choice=="Admin":
            logging.info(" Admin Selected..!!")
           
            
        else:
            st.write("Select Your Choice")
    except Exception as e:
        st.write(str(e))

main()
