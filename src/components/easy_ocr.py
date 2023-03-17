import easyocr
import os
import streamlit as st
from src import utils

class EasyOCR:
    def __init__(self):
        pass
    def extract_all_text(image_path):
        try:
            reader = easyocr.Reader(['en'])
            
            result = reader.readtext(image_path,detail = 0, paragraph=True)
            print(result)

            
            # name=EasyOCR.get_name(result)
            # return {"name":name}
            return result
        except Exception as e:
            st.error("error in extract_all_text"+ " " + str(e))
            


    def get_text_region_pixel(image_path):
        try:
            reader = easyocr.Reader(['en'])

            result=reader.readtext(image_path, paragraph=True)
            pixels=result[3]
            print(result[3])
            return pixels
        except Exception as e:
            st.error("error in get_text_region_pixel" + " " + str(e))


    def get_name(all_text_list):
        try:
            texl_list=all_text_list
            name=texl_list[0]
            return name
        except Exception as e:
            st.error("error in get_name" + " " + str(e))


    def get_mail(all_text_list):
        try:
            email=''
            for text in all_text_list:
                if "@" in text:
                    text_list=text.split()
                    for j in text_list:
                        if "@" in j:
                            email=j

            return email

        except Exception as e:
            st.error("error in get_mail" + " " + str(e))


    def get_number(all_text_list):
        try:
            number=''
            all_digit_list=[]
            for i in all_text_list:
                i_list=i.split()
                for j in i_list:
                    if j.isdigit():
                        all_digit_list.append(j)

            
            for num in all_digit_list:
                if len(str(num))>=10:
                    number=str(num)

            return number
        except Exception as e:
            st.error("error in get_number" + " " + str(e))
