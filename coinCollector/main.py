#Requirements :     make sure selenium and requests is installed 
#Install requets   :    pip install requests
# install selenium    :    pip install selenium

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import pickle

def min_time_find():
     end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0) 
     initial =  datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
     min_time_gap = end-initial
     return min_time_gap


def main():
     time_now = datetime.now()

     try:
          f = open("time.dat","rb")
          time_last = pickle.load(f)
          time_diff = time_now - time_last
          min_dif = min_time_find()
          if(time_diff < min_time_find):
               print("time left")
               time_to_wait = min_dif-time_diff
               time.sleep((time_to_wait.hour*60 + time_to_wait.minute)*60 +1)    
          
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


