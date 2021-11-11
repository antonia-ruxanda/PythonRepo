from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')

table_text = table.text
my_list = table.text.split('\n')

header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')
my_map = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(my_list), len(header)):
        my_map[header[int(j)]].append(my_list[i])

df = pd.DataFrame(my_map)
df.to_csv("BNR_ALL_DATA.xls")

time.sleep(10)
browser.close()
