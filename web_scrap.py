from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq

my_url='https://www.ncbi.nlm.nih.gov/pmc/?term=Iot'

uclient=ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html , "html.parser")

containers =page_soup.findAll("div" , {"class" : "rslt"})
container = containers

fil_nam="details.csv"
f = open("details.csv" , "w")
headers = "title,author,url\n"
f.write(headers)

for container in containers:
    topic =  container.find("div" , { "class" : "title"})
    topic_name = topic.text
    topic_name = topic_name.replace("," , "  ")

    author = container.find("div" , {"class" : "desc"})
    author_name = author.text
    author_name = author_name.replace("," , "  ")

    url = topic.a["href"]

    f.write(topic_name+","+author_name+","+url+"\n")

    print(topic_name+author_name+url)

f.close()

