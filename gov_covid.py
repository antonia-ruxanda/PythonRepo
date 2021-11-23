from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import pandas as pd
import datetime as dt
import unidecode

today = dt.datetime(2021, 1, 20)
week_ago = today - dt.timedelta(days=7)
str1 = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"
str2 = ""
str3 = "-ianuarie-ora-13-00/"
header = 'Nr. crt. Judet Numar de cazuri confirmate(total) Numar de cazuri nou confirmate Incidenta  inregistrata la ' \
         '14 zile '
header_text = re.findall('[A-Z][^A-Z]*', header)

my_dict = {i: [] for i in header_text}


for day in range(14, 21):
    str2 = str(day)
    link = str1 + str2 + str3
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    table = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]")
    table_text = table.text

    # new_list = rows of the table
    new_list = unidecode.unidecode(table_text).split('\n')
    new_list.pop(0)
    data = str2 + '.01.2021'
    new_list.insert(0, data + '    ')

    new_list[-2] = new_list[-2].replace("*", "")
    new_list[-2] = new_list[-2].strip() + " "
    new_list[-1] = " " + new_list[-1].strip() + " "

    # replace , . in xls standards
    new_list = [x.replace(',', '.') for x in new_list]
    new_list[-1] = new_list[-1].replace('.', ',')

    # separated all elements from the table
    # middle_list = separate the nr crt from table
    middle_list = [idx for i in new_list for idx in i.split(" ", maxsplit=1)]
    final_list = [idx[::-1] for i in middle_list for idx in reversed(i[::-1].split(" ", maxsplit=3))]
    print(final_list)

    for j in range(0, len(header_text)):
        for i in range(int(j), len(final_list), len(header_text)):
            my_dict[header_text[int(j)]].append(final_list[i])

    time.sleep(2)
    browser.close()

df = pd.DataFrame.from_dict(my_dict, orient='index')
df = df.transpose()
df.to_csv("Covid.xls")


