from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv


# Requests and reads the webpage
my_url = "https://www.glasgow.gov.uk/futureprocessions?fPst=1"
uClient = uReq(my_url)
page_of_protests = uClient.read()


soup = soup(page_of_protests, "html.parser")  # Parsing the html page
events_calendar = soup.find("table", {"id": "ProcessionsDiary"})


def create_dates_list():  # Makes list of calendar dates from the page
    weekday_dates = events_calendar.findAll(
        "td", {"class": "DiaryDayHeadingStyle"})
    weekend_dates = events_calendar.findAll(
        "td", {"class": "DiaryWeekendHeadingStyle"})
    dates_list = []
    for date in weekday_dates:
        dates_list.append(date.contents[0])

    for date in weekend_dates:  # Weekend dates have seperate class
        dates_list.append(date.contents[0])

    return dates_list


dates_list = create_dates_list()  # Storing list of calendar dates


def create_events_list():  # Creates list of events
    events = events_calendar.findAll("td", {"class": "DiaryDayStyle"})
    events_list = []
    for event in events:
        if event.contents[0].lower() == "no processions":
            events_list.append(event.contents[0])
        else:
            events_list.append(event.find(
                "tr", {"class": "DataGridItemStyle"}).td.contents[0])
    return events_list


events_list = create_events_list()  # Storing list of events


def create_assembly_points_list():  # Creates list of assembly points for events taking place
    events = events_calendar.findAll("td", {"class": "DiaryDayStyle"})
    locations_list = []
    for event in events:
        if event.contents[0].lower() != "no processions":
            location = events_calendar.find(
                "tr", {"class": "DataGridItemStyle"}).td.findNext("td").contents[0]
            locations_list.append(location)
        elif event.contents[0].lower() == "no processions":
            locations_list.append("No event")
    return locations_list


# Storing list of assembly points
assembly_points_list = create_assembly_points_list()

# Transpose from rows to columns for the csv
columns = zip(events_list, dates_list, assembly_points_list)

with open('processions.csv', 'w', newline='') as csvfile:  # Creates and writes csv file
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Event', 'Date', 'Assembly'])
    for column in columns:
        csv_writer.writerow(column)

csvfile.close()
