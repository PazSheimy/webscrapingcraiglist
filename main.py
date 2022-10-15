import requests
from bs4 import BeautifulSoup

URL = "https://fortmyers.craigslist.org/search/marco-island-fl/hhh?sort=date&purveyor=owner&max_bedrooms=4&lat=25.9875&lon=-81.6726&search_distance=13"
page = requests.get(URL)

print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="rows")
print(results.prettify())

house_elements = results.find_all('li', class_="result-row")
for house_elem in house_elements:
     #print(house_elem)
     price_elem = house_elem.find('span', class_='result-price')
     url_elem = house_elem.find('a', class_="result-image gallery")['href']
     title_elem = house_elem.find('a', class_="result-title hdrlnk")
     print(title_elem.text.strip())
     print(url_elem)
     print(price_elem.text.strip())
     print()

HOUSE_URL = "https://fortmyers.craigslist.org/col/vac/d/marco-island-marco-island-anglers-cove/7545500238.html"
HOUSE_PAGE = requests.get(HOUSE_URL)
house_soup = BeautifulSoup(HOUSE_PAGE.content, 'html.parser')

attributes = house_soup.find_all('p', class_='attrgroup')
for attribute in attributes:
    spans = attribute.find_all('span')
    for span in spans:
         text = span.text.strip()
         print(text)

posting_body = house_soup.find('section', {'id':'postingbody'})
print(posting_body.text)
