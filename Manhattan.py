__author__ = 'bcallander'

import requests
from bs4 import BeautifulSoup
import json
import time

with requests.Session() as c:

    url = 'http://lg.logistics.com/manh/index.html'
    USERNAME = 'RDC1VDEI'
    PASSWORD = 'ICETEA@5C'

    form_data = {
        'j_username': USERNAME,
        'j_password': PASSWORD
    }

    urx = 'https://mip.logistics.com/login.jsp'
    m = c.post(urx)
    print(m.headers)

    c.headers.update({'set-cookie': m.headers['set-cookie']})
    c.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'})
    c.headers.update({'Host': 'lg.logistics.com'})
    print(c.headers)


    r = c.post('https://mip.logistics.com/j_spring_security_check', allow_redirects=True, data=form_data)
    l = c.get(url, allow_redirects=True)
    print(c.headers)




    soup1 = BeautifulSoup(l.content)

    NAME = soup1.find('input', {'type': 'hidden'}).attrs['name']
    VALUE = soup1.find('input', {'type': 'hidden'}).attrs['value']
    form_data2 = {
        NAME: VALUE
    }

    u = c.post('https://mip.logistics.com/profile/SAML2/POST/SSO', data=form_data2)

    l = c.post(url, allow_redirects=True)

    soup2 = BeautifulSoup(l.content)







    c.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'})
    c.headers.update({'Referer': 'http://lg.logistics.com/manh/index.html'})
    c.headers.update({'Cookie': 'BIGipServerPool_63.128.86.132_80=356212746.51250.0000; lg_JSESSIONID=nKDRXNALWF0UtP7-BK10ce9W'})
    c.headers.update({'Host': 'lg.logistics.com'})
    print(requests.utils.dict_from_cookiejar(c.cookies))
    t = c.post('http://lg.logistics.com/ofr/ra/jsp/WebOffers.jsp?windowId=screen-170861139')



    soup = BeautifulSoup(t.content)


    obj = open('testText.txt', 'w')
    obj.write(soup.prettify())
    obj.close()



    list_data = soup.findAll('tr', {'class': ['trow', 'taltrow']})

    for data in list_data:
        data_dict = {}
        check = data.find('td', {'colspan': '3'})
        if check == None:
            cells = data.find_all('br')
            data_dict['ID_Number'] = cells[0].text.replace('\n', '')
            data_dict['Status'] = cells[1].text.replace('\n', '')
            if len(cells[2].find_all('div')) == 2:
                data_dict['Sender'] = cells[2].find('div').attrs['title']
            else:
                data_dict["Sender"] = cells[2].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', ' ')

            data_dict['Origin'] = cells[3].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', ' ')
            if len(cells[4].find_all('div')) == 2:
                data_dict['Receiver'] = cells[4].find('div').attrs['title']
            else:
                data_dict["Receiver"] = cells[4].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', ' ')
            data_dict['Destination'] = cells[5].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', ' ')
            print(data_dict)












