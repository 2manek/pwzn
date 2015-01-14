#!/usr/bin/python3.4-
# -*- coding: utf-8 -*-
import requests
import pickle
import time
from multiprocessing.pool import ThreadPool

import hashlib

global adres
adres = "http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-b"
adres = "http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a"

response = requests.head(adres)
global resp_len
resp_len = int(response.headers['Content-Length'])

print(resp_len)

N=10
data = []
global step
step = int(resp_len/N)


def download(ii):
  global resp_len
  global step
  global adres

  request_range = (ii, min(resp_len, ii+step-1))
  response = requests.get(adres, 
               headers = {
                  "Range": "bytes={}-{}".format(*request_range)
              })
  
  return response


ff = list(range(0, resp_len, step))

p = ThreadPool(N)
try:
    start = time.monotonic()
    result = p.map(download, ff)
    print(result)
    print(time.monotonic() - start)
finally: 
    p.close()
    p.join()

m = hashlib.md5()
for i in result:
	m.update(i.content)

print(m.hexdigest())
