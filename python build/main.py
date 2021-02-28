import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")
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


def type_bot():
    for word in my_text:
        pyautogui.typewrite(word)


if page_loaded:
    driver.find_element_by_xpath('//*[@id="gwt-uid-1"]/a').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-17"]/table/tbody'
                                                                                 '/tr[2]/td/table/tbody/tr[ '
                                                                                 '1]/td/table/tbody/tr[1]/td/div/div')))
    my_text = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr['
                                           '1]/td/table/tbody/tr[1]/td/div/div').text
    input_box = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')

    while not timer_finished:
        input_box_class = input_box.get_attribute('class')
        if input_box_class == 'txtInput':
            timer_finished = True
            type_bot()