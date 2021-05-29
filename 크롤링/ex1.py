#정보수집_크롤링
    #1. ex1.py

#크롤링: 인터넷에서 데이터 추출

#1. BeautifulSoup 설치
from bs4 import BeautifulSoup as bs #html 읽는 메소드 -> bs.read()

import urllib.request as ur

url = 'http://quotes.toscrape.com/' # 사이트 주소
html = ur.urlopen(url)  # 사이트 주소 불러오기

soup = bs(html.read(), "html.parser")

print(soup.find_all('span')[0].text)

print(soup.find_all('span')[1].text)

for i in soup.find_all('span'):
    print(i.text)

for i in soup.find_all('div' , { 'class' : 'quote' }):
    print(i.text)
