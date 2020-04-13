from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.glasgow.gov.uk/futureprocessions?fPst=1"
uClient = uReq(my_url)
page_of_protests = uClient.read()

# html parser
soup = soup(page_of_protests, "html.parser")

# Makes list of dates on the calendar of the page
weekday_dates = soup.findAll("td", {"class": "DiaryDayHeadingStyle"})
weekend_dates = soup.findAll("td", {"class": "DiaryWeekendHeadingStyle"})

dates_list = []
for date in weekday_dates:
    dates_list.append(date.contents[0])

# Weekend dates have seperate class
for date in weekend_dates:
    dates_list.append(date.contents[0])

# Makes list of events on the calendar of the current page
events = soup.findAll("td", {"class": "DiaryDayStyle"})

events_list = []
for event in events:
    events_list.append(event.contents[0])

event_data_rows = soup.findAll("tr", {"class": "DataGidHeaderStyle"})
