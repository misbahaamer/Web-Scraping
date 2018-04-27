from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return e
    try:
        bsObj = soup(html, "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title =  getTitle("http://pythonscraping.com/pages/warandpeace.html")
if title == None:
    print ("title could not be found")
else:
    print(title)











    
    

