# ---------------------------------------------------
#! ----------- web scraping with selenium -----------
# ---------------------------------------------------
# ? control browser with selenium for automated testing
# ? download file from the internet
# ? subtitle download and add on your movies [ many modules ]
# ? get quotes from websites
# ? get gold and currencies rate
# ? get news from websites
# ---------------------------------------------------

# in video 141 the material was old so i stop in there

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# browser openning elzero.org website
browser.get("https://elzero.org")
browser.implicitly_wait(5)

# browser go to search input and write "Front-End Developer" in it
browser.find_element(By.CSS_SELECTOR, "#search").send_keys("Front-End Developer")

browser.implicitly_wait(5)
# browser go to search button and click on it
browser.find_element(By.CSS_SELECTOR, ".search-submit").click()


input("Press Enter to close the browser...")
