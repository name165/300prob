from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib


url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=k3"

web = ur.urlopen( url )
soup = bs(web.read(), "html.parser")
price = soup.find_all("span", {"class" : ""})
finded = "판매"

for i in price:
    b = finded in i.text
    if b:
        print("현재 모델 출시가 : ",i.text)