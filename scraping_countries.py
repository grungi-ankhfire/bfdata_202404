import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html5lib")

# names = []
# capitals = []
# areas = []
# populations = []
data = {
    "Country": [],
    "Capital": [],
    "Population": [],
    "Area": []
}


for element in soup.find_all("div", class_="country"):
    name = element.find("h3").text.strip()
    data["Country"].append(name)
    capital = element.find("span", class_="country-capital").text.strip()
    data["Capital"].append(capital)
    area = element.find("span", class_="country-area").text.strip()
    data["Area"].append(float(area))
    population = element.find("span", class_="country-population").text.strip()
    data["Population"].append(int(population))

df = pd.DataFrame(data)

print(df)

