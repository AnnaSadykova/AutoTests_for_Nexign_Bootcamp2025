from selenium import webdriver
from selenium.webdriver.common.by import By
from autocorrect import Speller
from urllib.parse import urljoin
import time

spell = Speller(lang='ru')

def check_spelling(text):
    spell = Speller(lang='ru')
    words = text.split()
    misspelled_words = []

    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha()).lower()
        if cleaned_word:
            if spell(cleaned_word) != cleaned_word:
                misspelled_words.append(cleaned_word)

    return misspelled_words

def get_page_text(browser, url):
    browser.get(url)
    time.sleep(2)
    return browser.find_element(By.TAG_NAME, "body").text

def get_all_links(browser, base_url):
    browser.get(base_url)
    time.sleep(2)

    links = set()
    for element in browser.find_elements(By.TAG_NAME, "a"):
        href = element.get_attribute("href")
        if href and href.startswith(base_url):
            links.add(href)
    return links

def main():
    base_url = "https://nexign.com/ru"
    browser = webdriver.Chrome()

    try:
        print(f"Проверка главной страницы: {base_url}")
        text = get_page_text(browser, base_url)
        misspelled = check_spelling(text)
        if misspelled:
            print(f"Ошибки на главной странице: {misspelled}")
        else:
            print("Ошибок на главной странице не найдено.")

        print("Поиск всех ссылок на главной странице...")
        links = get_all_links(browser, base_url)
        print(f"Найдено {len(links)} ссылок.")

        for link in links:
            print(f"Проверка страницы: {link}")
            text = get_page_text(browser, link)
            misspelled = check_spelling(text)
            if misspelled:
                print(f"Ошибки на странице {link}: {misspelled}")
            else:
                print(f"Ошибок на странице {link} не найдено.")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()