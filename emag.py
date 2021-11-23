from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')

get_elem = browser.find_element(By.ID, 'searchboxTrigger')
get_elem.send_keys('telefon')
get_elem.submit()

product = browser.find_element(By.CLASS_NAME, 'card-item')
print(product.text)
time.sleep(10)
browser.close()
