import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = {
    "country": [],
    "confirmed": [],
    "deaths": [],
    "continent": [],
}

data_iterator = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iterator).text.strip()
        confirmed = next(data_iterator).text.strip()
        deaths = next(data_iterator).text.strip()
        continent = next(data_iterator).text.strip()

        # Append Data to data{}.
        data["country"].append(country)
        data["confirmed"].append(int(confirmed.replace(",", "")))
        data["deaths"].append(int(deaths.replace(",", "")))
        data["continent"].append(continent)

    except StopIteration:
        break

df = pd.DataFrame(data)
# pd.set_option('display.max_row',None)
# print(df)

df.to_excel('covid_data.xlsx', index=False, engine='openpyxl')
