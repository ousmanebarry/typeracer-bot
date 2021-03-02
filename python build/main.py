import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# # # SETUP # # #
username = 'iamabot123'
password = 'ousmane'
number_of_games = 5
# # # SETUP # # #


driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")
driver.maximize_window()

page_loaded = False
timer_finished = False
delay = 3
count = 0


def web_driver_wait(xpath):
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))


def find_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


def type_bot(text):
    for word in text:
        pyautogui.typewrite(word, interval=0.001)


try:
    web_driver_wait('//*[@id="tstats"]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/a')
    driver.find_element_by_class_name('gwt-Anchor').click()
    driver.find_element_by_class_name('gwt-TextBox').send_keys(username)
    driver.find_element_by_class_name('gwt-PasswordTextBox').send_keys(password)
    driver.find_element_by_class_name('gwt-Button').click()
    web_driver_wait('//*[@id="gwt-uid-1"]/a')
    page_loaded = True
except TimeoutException:
    print("Page took too long to load!")
    driver.close()
    sys.exit()

if page_loaded:
    find_element('//*[@id="gwt-uid-1"]/a').click()
    for i in range(number_of_games):
        timer_finished = False
        web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                        '1]/td/table/tbody/tr[1]/td')
        my_text = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                               '1]/td/table/tbody/tr[1]/td').text
        web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
        input_box = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                                 '2]/td/input')

        while not timer_finished:
            input_box_class = input_box.get_attribute('class')
            if input_box_class == 'txtInput':
                timer_finished = True
                ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[contains(@id,'
                                                                                  '"gwt-uid-")]/table/tbody/tr['
                                                                                  '2]/td')).perform()
                input_box.click()
                type_bot(my_text)
                count += 1
                print(count)
                driver.implicitly_wait(10)
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'raceAgainLink')))
                find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a').click()
