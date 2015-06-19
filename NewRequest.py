__author__ = 'bcallander'

import requests
from bs4 import BeautifulSoup
import string
import json
import time
import sched

runtime = True

full_dict = []

while runtime:

    # account information, able to be changed across accounts
    USERNAME = 'SballenCC'
    PASSWORD = 'Acebaby1!'


    c = requests.Session()
    c.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'})
    c.headers.update({'Cookie': 'TrucksUserName=ValDivia;'})
    c.headers.update({'Host':'www.chrwtrucks.com'})
    c.headers.update({'Origin':'https://www.chrwtrucks.com'})
    c.headers.update({'Referer':'https://www.chrwtrucks.com/'})
    t = c.post('https://www.chrwtrucks.com/default.aspx?ReturnUrl=%2fApplications%2fTMC%2fSpotBids.aspx',allow_redirects=True)

    # parse base html to find form data
    soup1 = BeautifulSoup(t.content)

    STATE = soup1.find('input', {'id': '__VIEWSTATE'}).attrs['value']
    GEN = str(soup1.find('input', {'id': '__VIEWSTATEGENERATOR'}).attrs['value'])
    VALIDATION = str(soup1.find('input', {'id': '__EVENTVALIDATION'}).attrs['value'])

    url = 'https://www.chrwtrucks.com/default.aspx?ReturnUrl=%2fApplications%2fTMC%2fSpotBids.aspx'

    login_data = {
        '__VIEWSTATE': STATE,
        '__VIEWSTATEGENERATOR': GEN,
        '__EVENTVALIDATION': VALIDATION,
        'Login_External1$txtLogin': USERNAME,
        'Login_External1$txtPassword': PASSWORD,
        'ReturnUrl':'/Applications/TMC/SpotBids.aspx',
        'Login_External1$ibnLogin.x' : 63,
        'Login_External1$ibnLogin.y' : 17,
        'javascript':'enabled'
    }
    r = c.post(url, data=login_data)

    soup = BeautifulSoup(r.content)

    # parse html
    find_table = soup.find('table', {'width': '100%'})
    find_rows = find_table.find_all('tr')

    for rows in find_rows:
        find_ref = rows.find_all('a')
        if find_ref != []:
            word = find_ref[0].attrs['href']
            word = word.replace('/', '%2F')
            word = word.replace('\", \"', '&CarrierID=').replace('javascript:ShowSpotLoadDetails(\"', '')
            word = word.replace('\")', '').replace('==', '%3D%3D').replace('+', '%252B')
            word_ext = '%253D%253D&LoadNumber=' + word
            word = word.replace('%3D%3D&CarrierID=', '%253D%253D%26CarrierID%3d').replace('%3D%3D', '')
            word_ext = word_ext.replace('%252B', '%2b')
            word = 'https://www.chrwtrucks.com/default.aspx?ReturnUrl=%2fApplications%2fTMC%2fSpotBidDetail.aspx%3fLoadNumber%3d' + word + word_ext
            find_cells = rows.find_all('td')
            data = {}
            org = find_cells[0].text
            data['Origin'] = {}
            data['Origin']['State'] = org[-2:]
            data['Origin']['City'] = org[1:-4]
            dest = find_cells[1].text
            data['Destination'] = {}
            data['Destination']['State'] = dest[-2:]
            data['Destination']['City'] = dest[1:-4]
            data['Close D/T'] = find_cells[2].text[1:]

            data['HazMat'] = find_cells[5].text[1:]

            into = c.post(word, allow_redirects=True)
            l = c.post(word, data=login_data)
            soup2 = BeautifulSoup(l.content)
            table = soup2.find_all('table')
            rows = table[1].find_all('tr')
            date1 = rows[1].find_all('td')
            data['PickUp_Date'] = date1[3].text
            data['PickUp_Time'] = date1[4].text
            data['Weight'] = date1[5].text
            date2 = rows[2].find_all('td')
            data['Delivery_Date'] = date2[3].text
            data['Delivery_Time'] = date2[4].text

            line = open('DATA.txt', 'w')
            line.write(soup2.prettify())
            line.close()


            if data not in full_dict:
                json_data = json.dumps(data)
                full_dict.append(data)
                obj = open('JSON3.txt', 'a')
                obj.write(json_data + '\n')
                obj.close()

    # sleeps for 5 minutes
    time.sleep(300)









