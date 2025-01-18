from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.NAME, 'firstname').send_keys('Vladimir')
    browser.find_element(By.NAME, 'lastname').send_keys('Zaetc')
    browser.find_element(By.NAME, 'email').send_keys('vova@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'for2.2.8.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()