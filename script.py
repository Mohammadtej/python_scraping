from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Edge()
driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
driver.implicitly_wait(10)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
table = soup.find('table', {'id': 'table_id'})

# Print or process the dynamic content
# Find all rows in the table body
rows = table.find('tbody').find_all('tr')

# Iterate through the first five rows and extract the Bid Closing Date
for row in rows[:5]:
    closing_date = row.find_all('td')[4].text.strip()
    description = row.find_all('td')[3].text.strip()
    quest_no = row.find_all('td')[1].text.strip()
    print(f"Closing Date: {closing_date}")
    print(f"description: {description}")
    print(f"Quest No: {quest_no}")


