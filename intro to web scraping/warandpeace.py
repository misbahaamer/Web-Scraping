from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError

page_html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
page_obj = soup(page_html, "lxml")
nameList = page_obj.findAll("span", {"class" : "green"})
for name in nameList:
    print (name.get_text())
