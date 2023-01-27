from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input = browser.find_element(By.LINK_TEXT, "224592")
    input.click()
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys("Minsk")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Belorussia")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла