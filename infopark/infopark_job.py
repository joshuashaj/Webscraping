import requests
from bs4 import BeautifulSoup
import urllib3

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://infopark.in/companies/jobs/thrissur'
keywords = ['python', 'mern']
job_found = ""
for i in keywords:
    job_found = job_found + f" {i}"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Raises an error for bad HTTP responses
    print("Request successful!")
    res = response.content
except requests.exceptions.SSLError as ssl_error:
    print(f"SSL error occurred: {ssl_error}")
except requests.exceptions.RequestException as req_error:
    print(f"Request error occurred: {req_error}")

soup = BeautifulSoup(res, "html5lib")
f = open("job_thrissur.txt", "w", encoding="utf-8")
f.write(f"{soup.prettify()}")
f.close()


jobs = soup.find_all("div", {"class": "row company-list joblist"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("div", {"class": "jobs-comp-name"}).text.strip()
    last_date = job.find("div", {"class": "job-date"}).text.strip()
    f = open("job_main.txt", "a", encoding="utf-8")
    f.write(f"{title} {company_name} {last_date}\n{link}\n\n")
    f.close()
    for i in keywords:
        job_keyword = i.lower()
        title_lower = title.lower()
        title_word = title_lower.split()
        word_found = job_keyword in title_word
        if word_found:
            f = open(f"{job_found}.txt", "a", encoding="utf-8")
            f.write(f"{title} {company_name} {last_date}\n{link}\n\n")
            f.close()
