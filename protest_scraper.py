from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Requests and read the webpage
my_url = "https://www.glasgow.gov.uk/futureprocessions?fPst=1"
uClient = uReq(my_url)
page_of_protests = uClient.read()

# html parsing
soup = soup(page_of_protests, "html.parser")
events_calendar = soup.find("table", {"id": "ProcessionsDiary"})


def create_dates_list():
    # Makes list of calendar dates from the page
    today_date = events_calendar.find(
        "td", {"class": "DiaryTodayHeadingStyle"})

    weekday_dates = events_calendar.findAll(
        "td", {"class": "DiaryDayHeadingStyle"})
    weekend_dates = events_calendar.findAll(
        "td", {"class": "DiaryWeekendHeadingStyle"})
    dates_list = []
    dates_list.append(today_date.contents[0])

    for date in weekday_dates:
        dates_list.append(date.contents[0])
    # Weekend dates have seperate class
    for date in weekend_dates:
        dates_list.append(date.contents[0])

    return dates_list


dates_list = create_dates_list()
print(dates_list)
