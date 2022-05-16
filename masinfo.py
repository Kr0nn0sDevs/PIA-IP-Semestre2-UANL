rom bs4 import BeautifulSoup

import requests
import pandas as pd

urls='https://cnnespanol.cnn.com/tag/lebron-james/'

pa=requests.get(urls)

sou=BeautifulSoup(pa.content, 'html.parser')

noti=sou.find_all('h2', class_='news__data')

info2 = sou.find('h2').get_text()

y3=info2.split()


y2=y3[0:50:1],'\n', "Lebron James alcnaza los 36.000 puntos" ,'\n',"Lebron queda fuera de la temporada por covid"
