import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.common.exceptions import NoSuchElementException
import os


url="http://192.168.192.200:8090/"
accounts=[['1si17cs088','dert'],['1si17cs052','bsha'],['1si17cs078','aqzj'],['1si17cs059','zsop'],]
acCounter=0
driver = webdriver.Firefox(executable_path = "/home/rishabh/Documents/pythonProjects/wifiIDBruteforce/geckodriver")


def isInternetAvailable():
     try :
          url = "https://www.facebook.com"
          a=requests.get(url,allow_redirects=False)
          if a.headers['Connection']=='keep-alive':
               return True
          return False
     except :
          return False


def tryNext():
     global acCounter
     global accounts
     usrName=accounts[acCounter][0]
     pwd=accounts[acCounter][1]
     driver.get(url)
     driver.find_element_by_id('username').send_keys(usrName)
     driver.find_element_by_id('password').send_keys(pwd)
     driver.find_element_by_id('loginbutton').click()
     acCounter+=1

     


while 1:
     if not isInternetAvailable():
          tryNext()
          print("Login successful")
          sleep(600)
     else:
          print("internet Available will try later")
          sleep(60)
