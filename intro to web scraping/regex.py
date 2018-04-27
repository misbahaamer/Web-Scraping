from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError
import re

page_html = urlopen("http://pythonscraping.com/pages/page3.html")
page_obj = soup(page_html, "lxml")
#<img src="../img/gifts/img1.jpg">

images = page_obj.findAll("img", {"src" : re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])