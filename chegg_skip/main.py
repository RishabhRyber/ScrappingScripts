from selenium import webdriver
import credentials as cred
from time import sleep
import os

browser = webdriver.Firefox(executable_path="{}/geckodriver".format(os.getcwd()))

def login():
    global browser
    browser.get("https://www.chegg.com/auth?action=login")
    browser.find_element_by_id("emailForSignIn").send_keys(cred.userName)
    browser.find_element_by_id("passwordForSignIn").send_keys(cred.password)
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div/div[3]/div/oc-component/div/div/div/div[2]/div[1]/div[1]/div/form/div/div/div/footer/button").click()
    sleep(3)

def notOnLastPage():
    global browser
    text = browser.page_source
    print(text)
    # if "no" in text:
    #     return False
    return True
def skip():
    global browser
    try:
        skip = browser.find_element_by_css_selector(".sc-bbmXgH")
        skip.click()
        browser.find_element_by_xpath("/html/body/div[1]/main/footer/div/div/div[4]/div/div/div[1]/div/label[4]").click()
        browser.find_element_by_xpath("/html/body/div[1]/main/footer/div/div/div[4]/div/div/div[2]/button/span[1]").click()

    except:
        browser.get("https://expert.chegg.com/expertqna")


def main():
    login()
    browser.get("https://expert.chegg.com/expertqna")
    sleep(5)
    while notOnLastPage():
        sleep(5)
        skip()
    

if __name__ == "__main__":
    main()
