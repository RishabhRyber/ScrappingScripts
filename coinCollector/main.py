# Author : Papaji

#Requirements :     make sure selenium and requests is installed 
#Install requets   :    pip install requests
# install selenium    :    pip install selenium


import requests
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
import os
import pickle

time_now = datetime.now()
time_diff = 0
min_time_gap = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)-datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(min_time_gap)

try:
     f = open("time.dat","rb")
     time_last = pickle.load(f)
     time_diff = time_now - time_last
     print(type(time_diff))
except:
     f =  open("time.dat", "wb")
     pickle.dump(time_now,f)
     print("lol")

quit()
url="http://192.168.192.200:8090/"
accounts=[['usn','pwd'],['usn','pwd'],['usn','pwd'],['usn','pwd'],]
acCounter=0

#Replace {} with you current directory
driver = webdriver.Firefox(executable_path = "{}/geckodriver")


