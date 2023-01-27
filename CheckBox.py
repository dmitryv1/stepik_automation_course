from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/math.html"

try:
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    result = browser.find_element(By.ID, "answer")
    result.send_keys(y)
    find_checkbox = browser.find_element(By.ID, "robotCheckbox")
    find_checkbox.click()
    find_radio_button = browser.find_element(By.ID, "robotsRule")
    find_radio_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()




finally:
    time.sleep(5)
    browser.quit()