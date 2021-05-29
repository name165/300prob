

#신촌 기온 출력
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

지역 = input() + '날씨'

url = "https://search.naver.com/search.naver?ie=utf8&query=" + 지역
web = urllib.request.urlopen(url)
soup = bs(web.read(), "html.parser")
tag = soup.find('span', {"class" : "todaytemp"})

print(tag.text)

#미세먼지 출력
tag = soup.find('dd', {"class" : "lv1"})

print(tag.text)

#오존 지수 출력
tag = soup.find('dd', {"class" : "lv2"})

print(tag.text)