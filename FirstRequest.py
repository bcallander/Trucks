__author__ = 'bcallander'

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=q3nowgweeoxzry0fp4v5ep1b; main=01011BA1D6378C60D208FE1BE1F945CF60D2080008760061006C00640069007600690061002E760061006C00640069007600690061003A0043006800720069007300740069006E0061002B004D006F006E00610063006F003A002B003B00530065007400740069006E00670073003A0065006E002D00550053007C00550053007C00012F00FF; CHRWTrucksLoginTime=2015519154756; testCookie=TRUE',
    'Host': 'www.chrwtrucks.com',
    'Origin': 'https://www.chrwtrucks.com',
    'Referer': 'https://www.chrwtrucks.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
}


l = requests.get('https://www.chrwtrucks.com/Applications/TMC/SpotBids.aspx', headers=)
print(l.content)

with requests.Session() as c:

    url = 'http://www.chrwtrucks.com/Applications/LoadBoard/CarrierBoard.aspx'
    t = c.get(url)

    header = c.headers

    print(header)
    soup1 = BeautifulSoup(t.content)

    STATE = soup1.find('input', {'id': '__VIEWSTATE'}).attrs['value']
    GEN = soup1.find('input', {'id': '__VIEWSTATEGENERATOR'}).attrs['value']
    VALIDATION = soup1.find('input', {'id': '__EVENTVALIDATION'}).attrs['value']

    USERNAME = 'valdivia'
    PASSWORD = 'Icetea%405'

    login_data = {
        '__VIEWSTATE': '%2FwEPDwULLTE0NzIyMTE3MTUPZBYCAgMPZBYCAgIPZBYIAgUPFgIeA2ZvcgUYTG9naW5fRXh0ZXJuYWwxX3R4dExvZ2luZAIIDxYCHwAFG0xvZ2luX0V4dGVybmFsMV90eHRQYXNzd29yZGQCCQ8PZBYCHgpvbmtleXByZXNzBThkZXRlY3RjYXBzKGFyZ3VtZW50c1swXSwgJ0xvZ2luX0V4dGVybmFsMV9sYmxMb2dpblRleHQnKWQCDw8PFgIeBFRleHQFYFdlbGNvbWUgYmFjay4gIEVudGVyIHlvdXIgdXNlcm5hbWUgYW5kIHBhc3N3b3JkIHRvIHNlZSByZWFsLXRpbWUgZnJlaWdodCBvcHBvcnR1bml0aWVzIGFuZCBtb3JlLmRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1Mb2dpbl9FeHRlcm5hbDEkY2hrUmV0YWluVXNlcgUYTG9naW5fRXh0ZXJuYWwxJGlibkxvZ2luF5i2bbSg%2FheiKKHQ1W2pPMqT45g%3D',
        '__VIEWSTATEGENERATOR': GEN,
        '__EVENTVALIDATION': '%2FwEdAAV4MqZDhWEi6EzbIJg5oNqnjhAcrIsv2dkfhKeaucB%2BSLY%2BXjDldcXU2kHNrfxuO3KtLu6tPLOXo1sAkD1L8UeK6gm8TuVQOghNj7LM9P4ljwdOvBiRsVDX7YdqNjD9kKsR7L0c',
        'Login_External1$txtLogin': USERNAME,
        'Login_External1$txtPassword': PASSWORD
    }

    r = c.post(url, data=login_data)

    test = BeautifulSoup(r.content)

    print(test.prettify())

    new_page = c.get('https://www.chrwtrucks.com/Applications/TMC/SpotBids.aspx')

    soup = BeautifulSoup(new_page.content)

    # print(soup.prettify())
