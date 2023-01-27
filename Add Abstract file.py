from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/file_input.html"

try:
    get_link = browser.get(link)
    get_first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Vasya")
    get_last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Petrov")
    get_email = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("google@yahoo.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "somefile.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    get_submit_button = browser.find_element(By.CSS_SELECTOR, "button").click()


finally:

    time.sleep(5)

    browser.quit()
