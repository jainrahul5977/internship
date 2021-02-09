from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq
from selenium import webdriver
import os 
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


driver = webdriver.Chrome(chromedriver)

my_url='https://www.ncbi.nlm.nih.gov/pmc/?term=Iot'
driver.get(my_url)
page =1
fil_nam="details_new.csv"
f = open("details_new.csv" , "w")
headers = "title,author,url\n"
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
        except print(0):
            url = "not Available"
        

        f.write(topic_name+","+author_name+","+url+"\n")

        print(topic_name+author_name+url)
    
    page+=1
    url = "https://www.ncbi.nlm.nih.gov/pmc?"+str(sid)+str(page)
    #driver.find_element_by_id('EntrezSystem2.PEntrez.PMC.Pmc_ResultsPanel.Entrez_Pager.Page').click()
    driver.find_element_by_class_name('next').click()
    page_html=driver.page_source
    



f.close()
