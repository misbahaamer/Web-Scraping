from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError

my_url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_KOTHLPCG_2c1_w?node=172456&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-3&pf_rd_r=E9TE39PBZFSDN7GWPN8C&pf_rd_t=101&pf_rd_p=879b324b-47f9-446a-8a4f-4685c1c938da&pf_rd_i=541966'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "lxml")
containers = page_soup.findAll("div", {"class" : "s-item-container"}) 

container = containers[0]

for container in containers:
    try:
        brand = container.span.find_next_sibling().get_text()
        title = container.a.img["alt"]
        currency = container.sup.get_text()

    