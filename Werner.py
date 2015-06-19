__author__ = 'bcallander'


import requests
from bs4 import BeautifulSoup
import time
import json
import sys



full_dict = []

c = requests.Session()

url = 'https://eportal.werner.com/index.cfm'
USERNAME = 'PATELS'
PASSWORD = 'Soob53'

form_data = {
    'userid': USERNAME,
    'password': PASSWORD,
    'SUBMIT': 'Log In'
}

form_data2 = {
    'slot': 0
}

r = c.post(url, data=form_data)

l = c.get('https://eportal.werner.com/ltrace/index.cfm?app_id=1')
y = c.post('https://eportal.werner.com/ltrace/report/index.cfm', data=form_data2)


soup = BeautifulSoup(y.content)


table = soup.find('table', {'class': 'clean datatable'})
body = table.find('tbody')

rows = body.find_all('tr')

for row in rows:
    data = {}
    cells = row.find_all('td')
    data["Number"] = cells[0].text
    data['Trailer'] = cells[1].text
    data['Origin'] = cells[2].text
    data['Destination'] = cells[3].text
    data['Load Status'] = cells[4].text
    data['Load_Date'] = cells[5].text
    data['Appt_Date'] = cells[6].text
    data['Appt_Time'] = cells[7].text

    print(data)


