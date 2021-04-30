import requests
import csv
from bs4 import BeautifulSoup


url = "https://scrapethissite.com/pages/simple/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')

def getCountryiesList():
	allCountriesData = soup.find_all("div", class_="col-md-4 country")
	for country in allCountriesData:
		Name = country.find("h3", class_="country-name").text.strip()
		Capital = country.find("span", class_="country-capital").text.strip()
		Population = country.find("span", class_="country-population").text.strip()
		Area = country.find("span", class_="country-area").text.strip()
		with open('countries.csv', 'a+', newline='') as f:
			writer = csv.writer(f)
			writer.writerow([Name, Capital, Population, int(float(Area))])

getCountryiesList()



