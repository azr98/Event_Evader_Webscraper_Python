from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.glasgow.gov.uk/futureprocessions?fPst=1"
uClient = uReq(my_url)
page_of_protests = uClient.read()

# html parser
page_soup = soup(page_of_protests, "html.parser")

