    
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import re    
import PIL.Image
from pytesseract import pytesseract
import re
from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Entry
import time 
import os
import subprocess
import threading
import sys
import json
from datetime import datetime

patents = ['https://patents.google.com/patent/BRPI0805854']
matches = []
patent_citations = pd.DataFrame()
no_patent_citations = pd.DataFrame()


Page_number = []
Patent_Number = []
Patent_Citations = []
Ids_citations = []


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path_proppler = r"C:\Program Files (x86)\poppler-0.68.0\bin"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")
preferences = {"download.default_directory":"D:/Pedro/Documents/TCC/DOWN_PATENTS/"}

options.add_experimental_option('prefs', {
"download.default_directory": "D:\Pedro\Documents\TCC\DOWN_PATENTS", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

browser =  webdriver.Chrome(chrome_options=options,executable_path="C:\chromedriver.exe")


class main: 
    def __init__(self):    
        
        browseFiles()                                            
        
def browseFiles():
        
        patentLink = "https://patents.google.com/patent/BR0302988A/pt"
        DownloadPdfFile(patentLink)   
                                     
        
def pdf2img(file,name_patent):    
    
        try:                        
            name_pdf_patent = name_patent + '.pdf'
            pages_to_delete = [0] 
            infile = PdfFileReader(file, 'rb')
            output = PdfFileWriter()

            for i in range(infile.getNumPages()):
                if i not in pages_to_delete:
                    p = infile.getPage(i)
                    p.compressContentStreams()
                    output.addPage(p)
            new_name_pdf_patent = ('/home/rick/Imagens/Down_Patent/Converted_Downpatent/%s' % (name_pdf_patent))
            with open('/home/rick/Imagens/Down_Patent/Converted_Downpatent/%s' % (name_pdf_patent), 'wb') as f:
                output.write(f)
            
            print("CONVERSÃO 1 DE PÁGINA COMPLETA")
            images = convert_from_path(new_name_pdf_patent,dpi=100)                 
            Result_Page_number = []
            Result_Patent_Number = []
            Result_Patent_Citations = []
            Result_Ids_citations = []
            number_of_citations = 0            
            
            for i in range(len(images)):     
                if i!=-1:
                    images[i].save('/home/rick/Imagens/PATENTE/image_patent_'+str(i)+'.png', 'PNG')                                                          
                    img = PIL.Image.open('/home/rick/Imagens/PATENTE/image_patent_'+str(i)+'.png')                                    
                    pytesseract.tesseract_cmd = path_to_tesseract                  
                    text = pytesseract.image_to_string(img)                         
                    
                    patten = '[A-Z][A-Z] \d{6,12}'
                    patten_2 = "[A-Z][A-Z] \d{1}\W\d{3}\W\d{3}"      
                    patten_3 = '[A-Z][A-Z]\d{6,12}'
                    patten_4 = '[A-Z][A-Z][A-Z][A-Z]\d{6,12}'
                    patten_5 = '[A-Z][A-Z] \d{2,4}.\d{6,12}'                    
                    patten_6 = '[A-Z][A-Z] \d{6,12}.\d{1,2}'
                    
                    result = re.findall(patten, text[:-1])
                    result_2 = re.findall(patten_2, text[:-1])
                    result_3 = re.findall(patten_3, text[:-1])
                    result_4 = re.findall(patten_4, text[:-1])
                    result_5 = re.findall(patten_5, text[:-1])   
                    result_6 = re.findall(patten_6, text[:-1])   
                    
                    if result:                        
                        result = list(dict.fromkeys(result))                     
                        append_to_terminal_text(str(result))
                        number_of_citations =+ len(result)                                                  
                                                                  
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result))                    
                        Result_Ids_citations.append(result)
                         
                                                                                                                                                       
                    if result_2:                        
                        result_2 = list(dict.fromkeys(result_2))
                        append_to_terminal_text(str(result_2))
                        number_of_citations =+ len(result_2)                                                              
                                                   
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result_2))
                        Result_Ids_citations.append(result_2)
                         
                                                                                     
                    if result_3:                        
                        result_3 = list(dict.fromkeys(result_3))
                        append_to_terminal_text(str(result_3))
                        number_of_citations =+ len(result_3)                                                            
                                                   
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result_3))
                        Result_Ids_citations.append(result_3)
                         
                                                                                         
                    if result_4:                        
                        result_4 = list(dict.fromkeys(result_4))
                        append_to_terminal_text(str(result_4))
                        number_of_citations =+ len(result_4)                                                              
                                                   
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result_4))
                        Result_Ids_citations.append(result_4)
                         
                                                                                     
                    if result_5:                        
                        result_5 = list(dict.fromkeys(result_5))
                        append_to_terminal_text(str(result_5))
                        number_of_citations =+ len(result_5)                                                              
                                                   
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result_5))
                        Result_Ids_citations.append(result_5)
                         
                                                                                         
                    if result_6:                        
                        result_6 = list(dict.fromkeys(result_6))
                        append_to_terminal_text(str(result_6))
                        number_of_citations =+ len(result_6)                                                               
                                                   
                        Result_Patent_Number.append(name_patent)                    
                        Result_Page_number.append(i+1)                    
                        Result_Patent_Citations.append(len(result_6))
                        Result_Ids_citations.append(result_6)
                                                                                                                                                   
            
            for i in range(len(images)):   
                if i!=0:
                    path_to_remove = ("/home/rick/Imagens/PATENTE/image_patent_%s.png" % (str(i)))         
                    os.remove(path_to_remove)                                                                             
                    
        except Exception as e:            
            print(e)
            print(exception_traceback.tb_lineno)
            Page_number.append("ERROR 404")
            Patent_Number.append(name_patent)
            Patent_Citations.append("ERROR 404")
            Ids_citations.append("ERROR 404")                                
                       
        append_to_terminal_text("Numero de citações no documento: %i" % number_of_citations)  
        if sum(Result_Patent_Citations) != 0:
                Page_number.append(Result_Page_number)   
                Patent_Number.append("https://patents.google.com/patent/"+name_patent)                 
                Patent_Citations.append(sum(Result_Patent_Citations))
                Ids_citations.append(Result_Ids_citations)
                del Result_Page_number
                del Result_Patent_Citations 
                del Result_Ids_citations
                gc.collect()
                print("Patente analisada e registrada!")
        else:            
                Page_number.append(0)   
                Patent_Number.append("https://patents.google.com/patent/"+name_patent)                 
                Patent_Citations.append(0)
                Ids_citations.append(0)                
                del Result_Page_number
                del Result_Patent_Citations 
                del Result_Ids_citations
                gc.collect()        
        os.remove(new_name_pdf_patent)  
        append_to_terminal_text("=====================================")                                  
             
    
def DownloadPdfFile(patent_list):        
    if(pd.isna(patent_list)):
            print("OH SHIT! ELEMENTO NÃO RECONHECIDO")

    else:
            browser.get(patent_list)        

            if (len(browser.find_elements_by_xpath("//h3[@id='patentCitations']")) != 0):
                sleep(1)
                print("Patente do Google")
                Patent_Number_Web = []
                Patent_len_Web = []
                Page_Number_Web = []
                Patent_Citation_Web = []

                sleep(1)
                Patent_Number_Web.append(browser.find_element_by_xpath("//h2[@id='pubnum']").get_attribute('innerHTML')            )
                patents_web = browser.find_elements_by_xpath("//span[@class='td nowrap style-scope patent-result']/state-modifier[@class='style-scope patent-result']/a[@class='style-scope state-modifier']")
                number_of_citation = re.findall("([1-9]?\d|100)", browser.find_element_by_xpath("//h3[@id='patentCitations']").text)
                Page_Number_Web.append("ON GOOGLE")

                number = number_of_citation[0]
                Patent_len_Web.append(int(number))

                for i in patents_web:
                    Patent_Citation_Web.append(i.text)

                Page_number.append(Page_Number_Web)
                Patent_Number.append(Patent_Number_Web)
                Patent_Citations.append(Patent_len_Web)
                Ids_citations.append(Patent_Citation_Web[0:int(number)])

            else:
                try:
                    sleep(2)
                    pubnum = browser.find_element_by_xpath("//h2[@id='pubnum']").get_attribute('innerHTML')
                    Download_Button = browser.find_element_by_xpath("//a[text()=' Download PDF']").click()
                    sleep(2)
                    print("PDF BAIXADO")                    

                    path_text = 'D:/Pedro/Documents/TCC/DOWN_PATENTS/' + pubnum + '.pdf'
                    pdf2img(path_text,pubnum)
                    os.remove(path_text)

                except Exception as e:
                    print("Patente não possui PDF %s" % (e))      
                    Page_number.append("SEM PDF")   
                    Patent_Number.append(re.findall('[A-Z][A-Z]\d{6,12}', patent_list)[0])                 
                    Patent_Citations.append("SEM PDF")
                    Ids_citations.append("SEM PDF")

                                
    patent_citations['Page'] = Page_number
    patent_citations['Patent Number'] = Patent_Number
    patent_citations['Patent Citations']  = Patent_Citations
    patent_citations['ID of patent cited'] = Ids_citations        
    
    resultado = {"Page":str(Page_number[0]),"Patent Number":str(Patent_Number[0]),"Patent Citations":str(Patent_Citations[0]),"ID of patent cited":str(Ids_citations[0])}
    getDate = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
    #LOCAL DE SALVAR OS DADOS
    #ARQUIVO JSON É AUTOMATICAMENTE CRIADO
    pathJsonFile = ("D:/Pedro/Documents/TCC/PATENTE/result %s.json" % (getDate))
    jsonFile = open(pathJsonFile,"w")    
    json.dump(resultado,jsonFile)             
           
    print("DATABASE GERADO!")    
    sys.exit()
    

main()

    
    
