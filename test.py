from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://stepik.org/lesson/184253/step/2?unit=158843"
browser.get(link)
browser.execute_script("alert('Robots at work');")
alert = browser.switch_to.alert
time.sleep(3)
alert_text = alert.text
print(alert_text)
alert.accept()
alert1 = browser.execute_script("alert('Woohoo');")
browser.switch_to.ale
time.sleep(3)
