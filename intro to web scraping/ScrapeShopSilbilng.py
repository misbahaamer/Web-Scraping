from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError

page_html = urlopen("http://pythonscraping.com/pages/page3.html")
page_obj = soup(page_html, "lxml")

for sibling in page_obj.find("table", {"id" : "giftList"}).tr.next_siblings:
    print(sibling)