# -*- encoding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import json
import re
import datetime

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "http://www.ccee.org.br/portal/faces/pages_publico/inicio?_adf.ctrl-state=103st1nd9x_5&_afrLoop=15259409258640#!"

option = Options()
option.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

key = 'RA1255'

driver.implicitly_wait(10)  # in seconds

content = driver.find_element_by_xpath('//*[@id="tabelaPreco"]/tbody').text

print(content)

tokenized = content.split('\n')
tokenized = [sent.split() for sent in tokenized if sent]
print(tokenized)

df = pd.DataFrame(tokenized, columns = ['tipo/regiao','SE/CO','S','NE','N'])
print(str(df))
df.reset_index(drop=True, inplace=True)

df.to_csv(str(datetime.datetime.now())+'.csv', ';', index=False)
