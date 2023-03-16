
import PyPDF2
import pdfbox
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io 
import streamlit as st

class PdfToText:
    def pypdf_2(filename):
        try:
            all_words=''
            pdffileobj=open(filename,'rb')
            pdfreader=PyPDF2.PdfReader(pdffileobj)
            x=len(pdfreader.pages)
            # print(x)
            for i in range(x):

                pageobj=pdfreader.pages[i]
                text=pageobj.extract_text()
                all_words=all_words +" "+ text
                all_words=all_words.replace("\n"," ")
                # print(all_words)
            
            return all_words
        except Exception as e:
            return {"error":str(e)}

    def pdf_box(filename):
        try:
            all_words=''

            p = pdfbox.PDFBox()
            all_words=p.extract_text(filename)
            all_words=str(all_words).replace("\n"," ")
            print("pdfbox",all_words)
            
            return all_words
        except Exception as e:
            return {"error":str(e)}
        
    def pdf_miner(filename):
        try:
            if filename is not None:
                resource_manager = PDFResourceManager()
                fake_file_handle = io.StringIO()
                converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                with open(filename, 'rb') as fh:
                    for page in PDFPage.get_pages(fh,
                                                caching=True,
                                                check_extractable=True):
                        page_interpreter.process_page(page)
                        print(page)
                    text = fake_file_handle.getvalue()

                # close open handles
                converter.close()
                fake_file_handle.close()
                return text
            
        except Exception as e:
            return {"error":str(e)}