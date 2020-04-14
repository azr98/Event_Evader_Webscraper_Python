from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Requests and reads the webpage
my_url = "https://www.glasgow.gov.uk/futureprocessions?fPst=1"
uClient = uReq(my_url)
page_of_protests = uClient.read()

# Parsing the html page
soup = soup(page_of_protests, "html.parser")
events_calendar = soup.find("table", {"id": "ProcessionsDiary"})

# Makes list of calendar dates from the page


def create_dates_list():
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


# storing list of calendar dates
dates_list = create_dates_list()


assembly_points = []

# Creates list of events


def create_events_list():
    events = events_calendar.findAll("td", {"class": "DiaryDayStyle"})
    events_list = []
    for event in events:
        if event.contents[0].lower() == "no processions":
            events_list.append(event.contents[0])
        else:
            events_list.append(event.find(
                "tr", {"class": "DataGridItemStyle"}).td.contents[0])
            # events_list.append(event.find(
            #     "tr", {"class": "DataGridItemStyle"}).td.td.contents[0])
    return events_list


events_list = create_events_list()
print(events_list)

# print(events[-2].contents[0]) below
# <td class = "DiaryDayStyle" >
# <table border = "1" cellpadding = "4" cellspacing = "0" class = "DataGrid" rules = "all" >
# <tr class = "DataGridHeaderStyle" >
# <td width = "45%" > Organisation < /td >
# <td width = "45%" > Assembly Point < /td >
# <td width = "10%" > </td >
# </tr >
# <tr class = "DataGridItemStyle" >
# <td width = "45%" > *CANCELLED * GLASGOW ORANGE DEFENDERS FLUTE BAND - withdrawn < /td >
# <td width = "45%" > FERRY ROAD YOKER < /td >
# <td width = "10%" > <a href = "javascript:__doPostBack('ProcessionsDiary$ctl04$ctl02$ctl00','')" > More Info < /a > </td >
# </tr >
# </table >
# </td >
