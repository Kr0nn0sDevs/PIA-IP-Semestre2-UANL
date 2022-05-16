from bs4 import BeautifulSoup

import requests
import pandas as pd

url='https://www.buscabiografias.com/biografia/verDetalle/10117/LeBron%20James'

page=requests.get(url)
soup=BeautifulSoup(page.content, 'html.parser')

eq=soup.find_all('div', class_='table table-bordered')

info = soup.find('ul').get_text()

y=info.split()

x=y[0:11:1] ,'\n', y[11:22:1] ,'\n', y[22:24:1] ,'\n', y[24:31:1]  ,'\n', y[31:36:1], '\n', y[36:45:1] ,'\n', y[45:49:1] ,'\n', y[49:55:1]


inte="Christian Eduardo Rosales Gonzales \n Luis Fernando Guerrero Cavazos "
