from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value')
    value = str(math.log(abs(12 * math.sin(int(x.text)))))
    browser.find_element(By.ID, 'answer').send_keys(value)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()