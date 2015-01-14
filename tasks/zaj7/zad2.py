import requests
import pickle
import time
from multiprocessing.pool import ThreadPool

import bs4

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'uname':'foo','password':'bar'}
adres = "http://194.29.175.134:4444"

session = requests.Session()

resp    = session.post(adres+"/login", data=payload, allow_redirects=False)
# print(resp.cookies)
# print(resp.text)
resp    = session.get(adres) # ,headers=headers)
bs = bs4.BeautifulSoup(resp.text)

links = []
for l in bs.findAll('a'): 
	links.append(l.get('href'))

print(links)
resp = session.get(adres+links[0]) # ,headers=headers)
# session.get(adres)