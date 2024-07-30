import requests
from bs4 import BeautifulSoup


url = 'https://timesofindia.indiatimes.com/world'


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
f = open("News_header.html","w", encoding="utf-8")
f.write(soup.prettify())
f.close()

headings = soup.find_all("div",{"class":"WavNE"})

for heading in headings:
    text = heading.text
    print(text)
    print()