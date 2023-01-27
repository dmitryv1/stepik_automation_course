from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/selects1.html"

try:
   get_link = browser.get(link)
   get_element_1 = browser.find_element(By.ID, "num1")
   get_text = get_element_1.text
   get_element_2 = browser.find_element(By.ID, "num2")
   get_text1 = get_element_2.text
   sum = int(get_text) + int(get_text1)
   int_to_string = str(sum)
   get_dropdown = Select(browser.find_element(By.ID, "dropdown"))
   get_dropdown.select_by_visible_text(int_to_string)
   get_submit_button = browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(8)

    browser.quit()
