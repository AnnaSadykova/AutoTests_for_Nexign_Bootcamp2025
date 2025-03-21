from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

browser = webdriver.Chrome()
browser.get("https://nexign.com/ru")

page_text = browser.find_element(By.TAG_NAME, "body").text

target_word = "nexign"

word_count = len(re.findall(r'\b' + re.escape(target_word) + r'\b', page_text, flags=re.IGNORECASE))

print(f"Слово '{target_word}' встречается {word_count} раз(а) на главной странице.")

time.sleep(3)
browser.quit()