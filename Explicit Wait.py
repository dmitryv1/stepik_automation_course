from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import log,sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    def somex(x):
        return log(abs(12*sin(x)))
    get_link = browser.get(link)
    explicit_wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    submit_button = browser.find_element(By.ID, "book").click()
    get_x_value = browser.find_element(By.ID, "input_value")
    get_x_text = get_x_value.text
    print(get_x_text)
    result = somex(int(get_x_text))
    submit_result = browser.find_element(By.ID, "answer").send_keys(result)
    click_on_submit_button = browser.find_element(By.ID, "solve").click()

finally:

    time.sleep(12)
    browser.quit()