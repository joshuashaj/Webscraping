import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://infopark.in/companies/jobs/thrissur'
keywords = ['python','mern','php', 'react']

job_found = ""
for i in keywords:
    job_found = job_found + f" {i}"

f = open(f"{job_found}.txt","w")
f.write(f"JOBS FOUND FOR {job_found}\n\n\n")
f.close()

response = requests.get(url, verify=False)

res = response.content

soup = BeautifulSoup(res, "html5lib")

jobs = soup.find_all("div", {"class": "row company-list joblist"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("div", {"class": "jobs-comp-name"}).text.strip()
    last_date = job.find("div", {"class": "job-date"}).text.strip()
    for i in keywords:
        job_keyword = i.lower()
        title_lower = title.lower()
        title_word = title_lower.split()
        word_found = job_keyword in title_word
        if word_found:
            f = open(f"{job_found}.txt", "a", encoding="utf-8")
            f.write(f"{title} {company_name} {last_date}\n{link}\n\n")
            f.close()