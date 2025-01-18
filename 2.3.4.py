from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value')
    value = str(math.log(abs(math.sin(int(x.text)) * 12)))
    browser.find_element(By.ID, 'answer').send_keys(value)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()