import easyocr
import os

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
        except:
            pass


    def get_text_region_pixel(image_path):
        try:
            reader = easyocr.Reader(['en'])

            result=reader.readtext(image_path, paragraph=True)
            pixels=result[3]
            print(result[3])
            return pixels
        except:
            pass

    def get_name(all_text_list):
        try:
            texl_list=all_text_list
            name=texl_list[0][1]
            return name
        except:
            pass