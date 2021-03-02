import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")
driver.set_page_load_timeout(30)
page_loaded = False
timer_finished = False
delay = 3

try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'gwt-uid-1')))
    page_loaded = True
except TimeoutException:
    print("Page took too long to load!")
    driver.close()
    sys.exit()


def web_driver_wait(xpath):
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))


def find_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


def type_bot():
    for word in my_text:
        pyautogui.typewrite(word, interval=0.025)
    web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a')
    find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a').click()


if page_loaded:
    find_element('//*[@id="gwt-uid-1"]/a').click()
    while True:
        web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td')
        my_text = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                               '1]/td/table/tbody/tr[1]/td').text
        input_box = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')

        while not timer_finished:
            input_box_class = input_box.get_attribute('class')
            if input_box_class == 'txtInput':
                timer_finished = True
                type_bot()
                timer_finished = False
