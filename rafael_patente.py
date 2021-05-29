from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")#Não abre o navegador

browser =  webdriver.Chrome(chrome_options=options,executable_path='C:\chromedriver.exe')
browser.maximize_window()
URL = "https://patents.google.com/patent/BRPI9909409B1/pt?oq=PI9909409"

class main:
    def __init__(self):
     EnterThePage()   

def EnterThePage():
        print("Executando")
        browser.get(URL)

        cited_by = ''
        patent_citations = ''
        number_invetor = ''
        singles = ''
        titularidade = ''

        try:
            cited_by = browser.find_element_by_xpath(("//a[@href='#citedBy']")).get_attribute('innerHTML')
            print("Citados por: ", cited_by)
        except:
            print("Erro ao capturar 'citedBy' ")
        try:
            patent_citations = browser.find_element_by_xpath(("//a[@href='#patentCitations']")).get_attribute('innerHTML')
            print("Patente citations: ", patent_citations)
        except:
            print("Erro ao capturar 'patent_citations' ")
        try:
            single = browser.find_elements_by_id('cc')
            singles = []
            for sin in single:
                singles.append(sin.get_attribute('innerHTML'))
            print("Singles: ", singles)
        except:
            print("Erro ao capturar 'singles' ")
        try:
            #titularidade = browser.find_element_by_xpath(
            #"/html/body/search-app/search-result/search-ui/div/div/div/div/div/result-container/patent-result/div/div/div/div[1]/div[2]/section/application-timeline/div/div[6]/div[3]/state-modifier/a/span").get_attribute(
            #"innerHTML")
            titularidade = browser.find_elements_by_class_name("application-timeline")
            titulo = str(titularidade[0].text)
            nome = ""
            if(titulo.find("Application filed by")  != -1 ):
                index = titulo.find("Application filed by")
                for j in range(index, len(titulo)):
                    if(titulo[j] == "," or titulo[j] == "\n"):
                        break
                    nome = nome + titulo[j]
            print("Titularidade: ", nome)
        except:
            print("Erro ao capturar 'titularidade' ")




        try:
            #Por tudo que estã em classificação
            classificacao = browser.find_elements_by_class_name("code")
            print("Classificação: ")
        except:
            print("Erro ao capturar Patent scope")

        try:
            #Fazer a contagem das siglas
            patent_family = len(singles)
            print("Patent Family Size: ", patent_family)
        except:
            print("Erro ao capturar Patent family size")


        try:
            #Fazer a contagem das siglas
            claims = browser.find_element_by_xpath("//*[@id='claims']/h3/div[1]/div[1]/span").get_attribute("innerHTML")
            print("Claims: ", claims)
        except:
            print("Erro ao capturar claims")

        try:
            #browser.find_element_by_xpath("//*[@id='wrapper']/div[1]/div[2]/section/dl[1]/dd[2]/state-modifier").get_attribute(
                    #'data-inventor')
            number_invetor = browser.find_elements_by_class_name("style-scope patent-result")
            #print("Invetors: ", number_invetor[0].text)
        except:
            print("Erro ao capturar 'number_invetor'")

        try:
            val = "NAO"
            single = browser.find_elements_by_id('cc')
            PCT = "NAO"
            for sin in single:
                if sin.get_attribute('innerHTML') == "WO":
                    PCT = "SIM"
            print("PCT: ", PCT)
            if PCT == "NAO":
                for sin in single:
                    if sin.get_attribute('innerHTML') != "BR":
                        val = "SIM"

            print("Sem PCT, mas com algum depósito fora do Brasil: ", val)
        except:
            print("Erro ao capturar 'number_invetor'")


        try:
            #Pegar primeira classificação
            primeira_classificacao = browser.find_elements_by_class_name("classification-tree")
            print("Primeira Classificação: ", primeira_classificacao[0].text)
        except:
            print("Erro ao pegar primeira classificação")

        
        try:
            # Fazer as contagem das classificações
            patent_scope = browser.find_element_by_class_name("style-scope state-modifier")
            print("Patent scope0: ")
        except:
            print("Erro ao capturar Patent scope")




main()




