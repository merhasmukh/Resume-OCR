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
        if os.path.exists(filename+".txt"):
            with open(filename+".txt","a") as fb:
                for line in text:
                    fb.write(line+"\n")
                fb.close()
        else:
            with open(filename+".txt","a") as fb:
                for line in text:
                    fb.write(line+"\n")
                fb.close()

    except Exception as e:
        st.error("error in  create_txt_file")


# print(getDate())
# print(getTime())
