from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq
from selenium import webdriver
import os 
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


driver = webdriver.Chrome(chromedriver)
driver2 = webdriver.Chrome(chromedriver)

my_url='https://www.ncbi.nlm.nih.gov/pmc/?term=Iot'
base_url = 'https://www.ncbi.nlm.nih.gov'
driver.get(my_url)
page =1
fil_nam="details_final.csv"
f = open("details_final.csv" , "w")
headers = "title,author,url,abstract\n"
f.write(headers)

uclient=ureq(my_url)
page_html = uclient.read()
uclient.close()
sid =3
for page in range(400):

    #data=
    

    
    
    page_soup = soup(page_html , "html.parser")

    containers =page_soup.findAll("div" , {"class" : "rslt"})
    container = containers

    

    for container in containers:
        topic =  container.find("div" , { "class" : "title"})
        topic_name = topic.text
        topic_name = topic_name.replace("," , "  ")

        author = container.find("div" , {"class" : "desc"})
        try:
            author_name = author.text
        except :
            author_name = "not Available"
          

        author_name = author_name.replace("," , "  ")

        try:
            url = topic.a["href"]
            final_url = base_url + url
            driver2.get(final_url)
            content=driver2.page_source
            abstract_soup = soup(content , "html.parser")
            abstract_content = abstract_soup.find("p" , {"class": "p p-first-last"})
            abstract = abstract_content.text
            abstract = abstract.replace("," , "  ")
        except :
            url = "not Available"
        

        f.write(topic_name+","+author_name+","+url+","+abstract+"\n")

       
    
    page+=1
    url = "https://www.ncbi.nlm.nih.gov/pmc?"+str(sid)+str(page)
    #driver.find_element_by_id('EntrezSystem2.PEntrez.PMC.Pmc_ResultsPanel.Entrez_Pager.Page').click()
    driver.find_element_by_class_name('next').click()
    page_html=driver.page_source
    
    



f.close()
