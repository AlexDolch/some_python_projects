
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    def __init__(self, driver: str):
        print("Starting up...")
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
    
    def open_page(self, url: str):
        print(f"Opening:{url}")
        self.browser.get(url)
    
    def close_browser(self):
        print("Closing browser...")
        self.browser.close()


if __name__ == "__main__":
    browser = Browser("chromedriver")
    
    browser.open_page("http://www.python.org")
    time.sleep(5)
    
    browser.close_browser()
    time.sleep(10)

