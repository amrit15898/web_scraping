import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.iplt20.com/auction/2023")
soup = BeautifulSoup(web.content, "html.parser")

table = soup.find("table", class_="ih-td-tab auction-tbl")
print(table)
