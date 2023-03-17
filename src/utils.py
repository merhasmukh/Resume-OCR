import os 
import sys
import streamlit as st
    
from datetime import datetime



def getDate():
    try:
        date_now=datetime.now().date().strftime("%m-%d-%Y")

        return date_now
    except Exception as e:
        return str(e)
    
def getTime():
    try:
        time_now=datetime.now().time().strftime("%H:%M:%S")
        return time_now
    except Exception as e:
        return str(e)
    
def create_txt_file(filename,text):
    try:
        # text_file=filename+".txt"
        text_file=filename  
        print("text_file_path_2",text_file)

        if os.path.exists(text_file):
            with open(text_file,"a") as fb:
                for line in text:
                    fb.write(line+"\n")
                fb.close()
        else:
            with open(text_file,"a") as fb:
                for line in text:
                    fb.write(line+"\n")
                fb.close()

    except Exception as e:
        st.error(str(e))

        st.error("error in  create_txt_file")

def delete_file(filename):
    try:
        os.remove(filename)
        
    except Exception as e:
        st.error(str(e))
        st.error("error in  delete file")

def read_txt_file(filename):
    try:
        with open(filename,"r") as fr:
           text_list=fr.readlines()
           fr.close()

        return text_list
        
    except Exception as e:
        st.error(str(e))
        st.error("error in  delete file")


# print(getDate())
# print(getTime())
