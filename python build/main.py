from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import time
import pyautogui

driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")
delay = 10
page_loaded = False
timer_finished = False

try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'gwt-uid-1')))
    page_loaded = True
except TimeoutException:
    print("Page took too long to load!")
    driver.close()
    sys.exit()

if page_loaded:
    driver.find_element_by_xpath('//*[@id="gwt-uid-1"]/a').click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-17"]/table'
                                                                                     '/tbody/tr[2]/td/table/tbody/tr[ '
                                                                                     '1]/td/table/tbody/tr['
                                                                                     '1]/td/div/div')))
        my_text = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr['
                                               '1]/td/table/tbody/tr[1]/td/div/div').text
    except TimeoutException:
        print("Page took too long to load!")
        driver.close()
        sys.exit()

    while not timer_finished:
        current_time = driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr/td/table/tbody/tr/td[3]/div').text
        print(current_time)
        if current_time == ':00':
            timer_finished = True
            for word in my_text:
                pyautogui.write(word)
