from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

browser_driver = Service('/usr/bin/chromedriver')

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    
    page_to_scrape.get("https://sip.elfak.ni.ac.rs/")
    time.sleep(1)

    sipT = page_to_scrape.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]/ul/li[1]/p[1]")
    sip_markdown = sipT.text
    sipt = page_to_scrape.find_element(By.XPATH, '//*[@id="novosti"]')

    with open("sip.md", "w") as sip_file:
        sip_file.write(sip_markdown)

    height = sipt.size['height']
    width = sipt.size['width']

    
    desired_width = max(width, 1200)  

    desired_height = min(height, 1000)

    page_to_scrape.set_window_size(desired_width, desired_height)  

   
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", sipt)

    sipt.screenshot('sip.png')

finally:
    page_to_scrape.quit()
