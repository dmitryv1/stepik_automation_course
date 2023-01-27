from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"

try:
    def x_math(x):
        return log(abs(12*sin(x)))

    get_link = browser.get(link)
    find_x = browser.find_element(By.ID, "input_value")
    get_x_value = find_x.text
    x = int(get_x_value)
    res = x_math(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    find_answer_field = browser.find_element(By.ID, "answer").send_keys(res)
    click_on_checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    change_radion_button = browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    click_on_submit_button = browser.find_element(By.CSS_SELECTOR, "button").click()
    web = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(By.ID, "verify"))
                

finally:
    time.sleep(5)
    browser.quit()