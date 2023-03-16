
from src.logger import logging
import os
# import module
from pdf2image import convert_from_path
import streamlit as st


def pdf_2_image(file,fname):
    try:
        # Store Pdf with convert_from_path function
        images = convert_from_path(file)
        print("FILE>>>>>>>>>>",file)

        fname=fname.replace(".pdf","")
        
        os.makedirs(os.path.join("resume_data","pdf_to_image",fname),exist_ok=True)
        for i in range(len(images)):
        
            # Save pages as images in the pdf
            try:
               
                images[i].save("./resume_data/pdf_to_image/"+fname+"/"+'page'+ str(i) +'.jpg', 'JPEG')
            except FileNotFoundError as fne:
                return {"error":str(fne)}
            except Exception as e:
                return {"error":str(e)}

                  
       


        logging.info("PDF TO IMAGE CONVERTED SUCCESSFULLY....")
    except Exception as e:
        # log.log_fun(str(e))
        return {"error":"exception in pdf_2_image"}