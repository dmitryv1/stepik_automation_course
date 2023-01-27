from  selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    def xvalue(x):
        return log(abs(12*sin(x)))
    get_link = browser.get(link)
    click_button = browser.find_element(By.CSS_SELECTOR,"button").click()
    #Создание нового окна
    new_window = browser.window_handles[1]
    print(type(new_window))
    #Переключение на новую вкладку
    browser.switch_to.window(new_window)
    get_value = browser.find_element(By.ID, "input_value")
    x = get_value.text
    res = xvalue(int(x))
    send_values = browser.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(res)
    click_submit_button = browser.find_element(By.CSS_SELECTOR, "button").click()

finally:

    time.sleep(4)

    browser.quit()