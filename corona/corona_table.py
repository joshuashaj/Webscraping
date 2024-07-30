import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for scraping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = {
    "country": [],
    "confirmed": [],
    "deaths": [],
    "continent": [],
}

# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))

# while data_iterator:
#     print(next(data_iterator).text)

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
while True:
    try:
        country = next(data_iterator).text.strip()
        confirmed = next(data_iterator).text.strip()
        deaths = next(data_iterator).text.strip()
        continent = next(data_iterator).text.strip()

        data["country"].append(country)
        data["confirmed"].append(confirmed)
        data["deaths"].append(deaths)
        data["continent"].append(continent)

    except StopIteration:
        print("iteration stoped")
        break

# Create the DataFrame
df = pd.DataFrame(data)
pd.set_option('display.max_rows', None)

f=open("Corona_Table.txt","w",encoding="utf-8")
f.write(f"{df}")
f.close()
# print(df)
