#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
Day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
Time = ['Breakfast', 'Lunch', 'Dinner']
def jenna() :
    url = 'http://kwangju-s.hs.kr/xboard/board.php?tbnum=44'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    
    #aa = soup.find_all('td', class_=re.compile('yoil +'))
    menu = soup.find_all('td', class_=re.compile(' yoil+'))
    text = str(menu)
    print(text)
    start = []
    finish = []
    for m in re.finditer('sDay=">', text):
        index=m.end()
        start.append(index+1)
    
    for m in re.finditer('</a>', text):
        index=m.start()
        finish.append(index-1)

    for i in range(6):
        sub = text[start[i]:finish[i]]
        item = sub.split("<br/>\n<br/>")
        print('<',Day[i],'>')
        for j in range(3):
            print('{',Time[j],'}')
            print(item[0].replace("<br/>",""))
            
        print('--------------------------------')
            
jenna()
