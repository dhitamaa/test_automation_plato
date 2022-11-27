import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

def test_failed_register_with_invalid_password():
    # steps
    browser.get("https://en-gb.facebook.com/reg/") # open url
    browser.find_element(By.NAME,'firstname').send_keys("Andika") #input firstname
    browser.find_element(By.NAME,'lastname').send_keys("Pratama") #input lastname
    browser.find_element(By.NAME,'reg_email__').send_keys("dhitamadesu@gmail.com") #input email
    browser.find_element(By.NAME,'reg_email_confirmation__').send_keys("dhitamadesu@gmail.com") #re-input email
    browser.find_element(By.NAME,'reg_passwd__').send_keys("dhitamadesu")  # input password 
    browser.find_element(By.NAME,"birthday_day").click() # input day of birhtday
    browser.find_element(By.XPATH,'//*[@id="day"]/option[28]').click() # click day
    browser.find_element(By.NAME,"birthday_month").click() # input month of birhtday
    browser.find_element(By.XPATH,'//*[@id="month"]/option[5]').click() # click month
    browser.find_element(By.NAME,"birthday_year").click() # click year
    browser.find_element(By.XPATH,'//*[@id="year"]/option[23]').click()# input year of birhtday
    browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input').click() # choose gender
    browser.find_element(By.NAME,'websubmit').click() # click submit

    # Validation 
    time.sleep(2)
    assert browser.find_element(By.ID, "reg_error_inner").text == 'Your email address cannot be your password. Please enter at least six letters and numbers.'
