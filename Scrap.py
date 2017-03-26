import requests
import os
from bs4 import BeautifulSoup

url = 'https://null.co.in/upcoming'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table',{'class':'table table-condensed'})
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        for span in cell.find_all('span',{'class':'label label-success'}):
               t = soup.find_all('a',{'href':'/chapters/1-bangalore'})
print t
count = len(t)-1
c = str(count)
print count
up = 'Upcoming Bangalore Events'
title = 'Bangalore Upcoming events'
os.system('notify-send "'+title+" "+c)
