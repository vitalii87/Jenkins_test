from selenium import webdriver
from time import sleep
import pytest
import urllib.request
import time
import requests
#
# driver = webdriver.Firefox()
# driver.get("http://development.nxte.nl/Cadeau_Concepten/CACO1708-CadeauService/my-cadeauservice")
# #cookie = {'‘name’ : ‘foo’, ‘value’ : ‘bar’'}
# co = driver.get_cookies()
# sleep(2)
# driver.close()
# print(co)
#
# def myfunc():
#     raise ValueError("Exception 123 raised")
#
# def test_match():
#     with pytest.raises(ValueError, match=r'.* 123 .*'):
#         myfunc()
#
# print(test_match())

nf = urllib.request.urlopen('http://ruex.eu/account/login')
start = time.time()
page = nf.read()
end = time.time()
nf.close()

# a = requests.get("http://development.nxte.nl/Cadeau_Concepten/DKK1801-ETOS/zoekresultaat").elapsed.total_seconds()
# b = requests.get("http://ruex.eu/account/login").elapsed.total_seconds()
# print(a, b)

