import requests
import pandas as pd
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq

my_url='https://www.ncbi.nlm.nih.gov/pmc/?term=Iot'
base_url = 'https://www.ncbi.nlm.nih.gov/pmc/?term=Iot'

urls = []
urls.append(base_url)

url = urls.pop(0) # removes the first element from the list of urls
uclient=ureq(url)
page_html = uclient.read()
uclient.close()
soup_s = soup(page_html , "html.parser")
next_url = soup_s.find('a', class_= "active page_link next") # finds the next urls to crawl
if next_url: # if it's not an empty string
    urls.append(base_url + next_url['href'])
print(urls)
'''
#print(len(urls))
fil_nam="details_new.csv"
f = open("details_new.csv" , "w")
headers = "title,author,url\n"
f.write(headers)

while len(urls) > 0: # while we have urls to crawl
    #print(urls)
    url = urls.pop(0) # removes the first element from the list of urls
    uclient=ureq(url)
    page_html = uclient.read()
    uclient.close()
    soup_s = soup(page_html , "html.parser")
    next_url = soup_s.find('a', class_= "active page_link next") # finds the next urls to crawl
    if next_url: # if it's not an empty string
        urls.append(base_url + next_url['href']) # adds next url to crawl to the list of urls to crawl
    containers =soup_s.findAll("div" , {"class" : "rslt"})
    container = containers

    

    for container in containers:
        topic =  container.find("div" , { "class" : "title"})
        topic_name = topic.text
        topic_name = topic_name.replace("," , "  ")

        author = container.find("div" , {"class" : "desc"})
        author_name = author.text
        author_name = author_name.replace("," , "  ")

        url = topic.a["href"]

        f.write(topic_name+","+author_name+","+url+"\n")

        #print(topic_name+author_name+url)

f.close()
'''