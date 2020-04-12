from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.glasgow.gov.uk/futureprocessions"
uClient = uReq(my_url)
page_of_protests = uClient.read()

# html parser
soup = soup(page_of_protests, "html.parser")

dates = soup.findAll("td", {"class": "DiaryDayHeadingStyle"})


dates_data = []

for date in dates:
    dates_data.append(date.contents[0])

print(dates_data)
