import sys
import pyautogui
from setup.setup import username, password, number_of_games
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Opens website and maximizes window
driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")
driver.maximize_window()

# Important Variables
page_loaded = False
timer_finished = False
delay = 3


# Function to wait for presence of an element
def web_driver_wait(xpath):
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))


# Function to find an element
def find_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


# Function to type the text
def type_bot(text):
    for word in text:
        pyautogui.typewrite(word, interval=0.001)

    driver.implicitly_wait(10)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'raceAgainLink')))
    find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a').click()


# Logging In
try:
    web_driver_wait('//*[@id="tstats"]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/a')
    driver.find_element_by_class_name('gwt-Anchor').click()
    driver.find_element_by_class_name('gwt-TextBox').send_keys(username)
    driver.find_element_by_class_name('gwt-PasswordTextBox').send_keys(password)
    driver.find_element_by_class_name('gwt-Button').click()
    web_driver_wait('//*[@id="gwt-uid-1"]/a')
    page_loaded = True
# Outputs error and exits if the page takes too long to load
except TimeoutException:
    print("Page took too long to load!")
    driver.close()
    sys.exit()

# If the page is loaded
if page_loaded:
    # Clicks on 'play' button
    find_element('//*[@id="gwt-uid-1"]/a').click()
    # For loop for the number of times the person wants the bot to play the game
    for i in range(number_of_games):
        # Gets the text and class of the input box
        timer_finished = False
        web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                        '1]/td/table/tbody/tr[1]/td')
        my_text = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                               '1]/td/table/tbody/tr[1]/td').text
        web_driver_wait('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
        input_box = find_element('//*[contains(@id,"gwt-uid-")]/table/tbody/tr[2]/td/table/tbody/tr['
                                 '2]/td/input')
        # While the timer is not finished
        while not timer_finished:
            # Keeps checking the class of the input box
            input_box_class = input_box.get_attribute('class')
            # If the input changes to 'txtInput'
            if input_box_class == 'txtInput':
                # Scrolls down for the input box to be in view
                timer_finished = True
                ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[contains(@id,'
                                                                                  '"gwt-uid-")]/table/tbody/tr['
                                                                                  '2]/td')).perform()
                # Clicks the input box and starts typing
                input_box.click()
                type_bot(my_text)

