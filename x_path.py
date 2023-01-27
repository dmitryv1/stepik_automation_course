from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    get_link = browser.get(link)
    get_first_name = browser.find_element(By.NAME, "first_name")
    get_first_name.send_keys("Vasya")
    get_last_name = browser.find_element(By.NAME, "last_name")
    get_last_name.send_keys("Pupkin")
    get_city = browser.find_element(By.CLASS_NAME, "city")
    get_city.send_keys("Popovka")
    get_country = browser.find_element(By.ID, "country")
    get_country.send_keys("Winterfall")
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:

    time.sleep(7)

    browser.quit()

