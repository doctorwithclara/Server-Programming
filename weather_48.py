#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def jenna() :
    url = 'http://www.kma.go.kr/weather/forecast/timeseries.jsp?searchType=INTEREST&wideCode=2900000000&cityCode=2917000000&dongCode=2917069500'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    text = str(soup)
    
    pattern = "now_weather1"
    match = re.search(pattern, text)
    startIndex = match.end()
 
    pattern = "time_weather1"
    match = re.search(pattern, text)
    endIndex = match.start()
    clean=text[startIndex:endIndex].split("</dd>")
    for m in clean:
        final = m.split(">")
        print(final[1])
jenna()
