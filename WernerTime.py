__author__ = 'bcallander'


import requests
from bs4 import BeautifulSoup
import time
import json


full_dict = []

with requests.Session() as c:
