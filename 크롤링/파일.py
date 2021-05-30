

# 현재 은 가격 크롤링
from bs4 import BeautifulSoup as bs
import urllib.request as ur


url = "https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_GC&fdtc="
web = ur.urlopen(url)
soup = bs( web.read(), "html.parser")

a = soup.find_all("tr", {"class" : "up"})

print(a[1].text[3:8])