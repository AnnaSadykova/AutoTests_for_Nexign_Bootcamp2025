import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    browser = webdriver.Chrome()
    link = "https://nexign.com/ru"
    browser.get(link)

    products = browser.find_element(By.XPATH, "//span[text()='Продукты и решения']")
    products.click()
    time.sleep(3)

    products_instruments = browser.find_element(By.XPATH, "//span[text()='Инструменты для ИТ-команд']")
    products_instruments.click()
    time.sleep(3)

    products_instruments_nord = browser.find_element(By.XPATH, "//a[text()='Nexign Nord']")
    products_instruments_nord.click()
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()