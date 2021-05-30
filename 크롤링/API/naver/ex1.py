#api: 미리 만들어둔 코드/프로그램

#1 네이버 로그인
#2 네이버 api 검색 -> 네이버 개발자 센터
#3 사이드 메뉴에서 어플리케이션 -> 등록

#4 사이트 메뉴 => Document
#5 검색 결과 딕셔너리 호출 [데이터 가공]
    #결과 : {"item":"검색결과리스트"}

#발급받은 애플리케이션 정보를 변수에 저장
import os
import sys
import urllib.request
import json
import re
client_id = "o29ZhA_qIoynZire1FP4"
client_secret = "cMjRJJ5Vl6"
search = input("블로그 검색 : ")
encText = urllib.parse.quote(search)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')

    json결과 = json.loads(검색결과)

    결과리스트 = []
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print(타이틀)
else:
    print("Error Code:" + rescode)

search = input("책 검색 : ")
encText = urllib.parse.quote(search)
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')

    json결과 = json.loads(검색결과)

    결과리스트 = []
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print(타이틀)

else:
    print("Error Code:" + rescode)

search = input("뉴스 검색 : ")
encText = urllib.parse.quote(search)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')

    json결과 = json.loads(검색결과)

    결과리스트 = []
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print(타이틀)
else:
    print("Error Code:" + rescode)