from bs4 import BeautifulSoup as bs
import urllib.request as ur

#크롤링 할 주소 저장
url = "https://movie.naver.com/movie/running/current.nhn"

#주소 열어서 web 저장
web = ur.urlopen(url)

#web 변수 읽기
soup = bs(web.read(), "html.parser")

#해당 태그 찾기
tag = soup.find_all('ul', {"class" : "current_list"})

print(tag)

#영화 랭킹 크롤링 하기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
web = ur.urlopen(url)
soup = bs(web.read(), "html.parser")
tag = soup.find_all("div", {"class" : "tit3"})
print(tag)
