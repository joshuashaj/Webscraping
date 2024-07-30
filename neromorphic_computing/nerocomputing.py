import requests
import urllib3
from bs4 import BeautifulSoup
import lxml

url = 'https://www.ibm.com/think/topics/neuromorphic-computing'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


try:
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Raises an error for bad HTTP responses
    print("Request successful!")
except requests.exceptions.SSLError as ssl_error:
    print(f"SSL error occurred: {ssl_error}")
except requests.exceptions.RequestException as req_error:
    print(f"Request error occurred: {req_error}")

soup = BeautifulSoup(response.content,"lxml")
f=open("nerocomputing.html","w")
f.write(f"{soup}")
f.close()

para = soup.find_all("div",{"class":"complex-narrative"})
for par in para:
    paragragh = par.find("p")
    paragragh_text = paragragh.text
    # print()
    f = open("nerocomputing.txt", "w")
    f.write(f"{paragragh_text}")
    f.close()
