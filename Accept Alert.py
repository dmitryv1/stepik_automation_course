from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from math import  log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


try:
    def somef(x):
        return log(abs(12*sin(x)))
    get_link = browser.get(link)
    confirm_button = browser.find_element(By.CSS_SELECTOR, "button").click()
    alert_accept = browser.switch_to.alert
    alert_accept.accept()
    get_input_value = browser.find_element(By.ID, "input_value")
    x = get_input_value.text
    define_value = somef(int(x))
    send_to_field = browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(define_value)
    click_submit_button = browser.find_element(By.CSS_SELECTOR, "button").click()


finally:

    time.sleep(5)

    browser.quit()