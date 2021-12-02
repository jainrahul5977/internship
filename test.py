from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq
from selenium import webdriver
import os 
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


driver = webdriver.Chrome(chromedriver)

my_url='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5677444/'
base_url = 'https://www.ncbi.nlm.nih.gov'
driver.get(my_url)
content=driver.page_source
abstract_soup = soup(content , "html.parser")
abstract_container = abstract_soup.find("p" , {"class": "p p-first-last"})
abstract = abstract_container.text
print(abstract)
'''
fil_nam="details_new.csv"
f = open("details_new.csv" , "w")
f.write(topic_name+","+author_name+","+url+"\n")
'''