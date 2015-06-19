__author__ = 'bcallander'


import requests
from bs4 import BeautifulSoup
import json
import time
import sys


full_dict = []

def parse(soup):
            table = soup.find('table', {'id': "ctl00_cphCustomerContent_dgOrderAvailable"})

            rows = table.find_all('tr')

            for row in rows:
                find_cells = row.find_all('td')
                brk = row.find('br')
                data = {}
                if brk != None:
                    org = find_cells[0].find('br').text.replace(' ', '')
                    data['Origin'] = {}
                    data['Origin']['City'] = org[:-3]
                    data['Origin']['State'] = org[-2:]
                    dest = find_cells[1].find('br').text.replace(' ', '')
                    data['Destination'] = {}
                    data['Destination']['City'] = dest[:-3]
                    data['Destination']['State'] = dest[-2:]
                    data['Weight'] = find_cells[2].text
                    # miles = find_cells[3].text
                    # if miles == ' ':
                        # miles = 'N/A'
                    # data['Distance'] = miles
                    data['Departure'] = find_cells[4].text
                    arrive = find_cells[5].text
                    if arrive == ' ':
                        arrive = data['Departure']
                    data['Arrival']= arrive
                    data["Trailer_Code"] = find_cells[6].text


                    print(data)

                    if data not in full_dict:
                        json_data = json.dumps(data)
                        full_dict.append(data)
                        obj = open('ADMJSON.txt', 'a')
                        obj.write(json_data + '\n')
                        obj.close()

with requests.Session() as c:

    USERNAME = 'w133355'
    PASSWORD = 'Michelle13'

    url = 'https://www.e-adm.com/login.asp'

    form_data = {
        'Login': USERNAME,
        'Password': PASSWORD,
        'Submit': 'Login >>',
        'FormAction': 'Login >>',
        'URL': '/default.asp?'
    }

    r = c.post(url, data=form_data)

    l = c.get('https://www.e-adm.com/fltendExternal/fltUserAvailableOrders.aspx?QLink=')

    soup = BeautifulSoup(l.content)

    parse(soup)

    for num in range(5):


        VIEWSTATE = soup.find('input', {'name': '__VIEWSTATE'}).attrs['value']
        GENERATOR = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).attrs['value']
        EVENT = soup.find('input', {'name': '__EVENTVALIDATION'}).attrs['value']


        form_data2 = {
            '__EVENTTARGET': 'ctl00$cphCustomerContent$NextPage',
            'ctl00_cphCustomerContent_ScriptManager1_HiddenField': ';;AjaxControlToolkit, Version=4.1.51116.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:fd384f95-1b49-47cf-9b47-2fa2a921a36a:de1feab2:f9cec9bc:a0b0f951:a67c2700:fcf0e993:f2c8e708:720a52bf:589eaa30:698129cf:fb9b4c57:ccb96cf9',
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': GENERATOR,
            '__EVENTVALIDATION': EVENT
        }

        y = c.post('https://www.e-adm.com/fltendExternal/fltUserAvailableOrders.aspx?QLink=', data=form_data2)

        soup = BeautifulSoup(y.content)

        parse(soup)