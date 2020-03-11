
from bs4 import BeautifulSoup
import requests
URL='https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
rows = soup.find_all('p')
for row in rows:          # Print all occurrences
    print(row.get_text())