from selenium import webdriver
from time import sleep
import pyautogui
import pytesseract
from PIL import Image

driver = webdriver.Chrome(executable_path="/Users/Owner/Documents/chromedriver.exe")
driver.get("https://play.typeracer.com/")

driver.find_element_by_xpath('//*[@id="gwt-uid-1"]/a').click()
