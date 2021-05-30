import os
import sys
import urllib.request
import json
import re
client_id = "o29ZhA_qIoynZire1FP4"
client_secret = "cMjRJJ5Vl6"
url = "https://openapi.naver.com/v1/search/movie.json"
option = "&display=1&sort=count"
query = "?query="+urllib.parse.quote(input("검색 : "))
url_query = url + query + option
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    res = response_body.decode('utf-8')

    jsonres = json.loads(res)

    result = []

    for i in jsonres['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        감독 = re.sub('<.+?>', '', i['director'], 0, re.I | re.S)
        배우 = re.sub('<.+?>', '', i['actor'], 0, re.I | re.S)
        평점 = re.sub('<.+?>', '', i['userRating'], 0, re.I | re.S)
        print(타이틀+"|"+감독+배우+평점)
else:
    print("Error Code:" + rescode)

print()

url = "https://openapi.naver.com/v1/search/book.json"
option = "&display=1&sort=count"
query = "?query="+urllib.parse.quote(input("검색 : "))
url_query = url + query + option
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    res = response_body.decode('utf-8')

    jsonres = json.loads(res)

    result = []

    for i in jsonres['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        작가 = re.sub('<.+?>', '', i['author'], 0, re.I | re.S)
        출판사 = re.sub('<.+?>', '', i['publisher'], 0, re.I | re.S)
        print(타이틀+"|"+작가+"|"+출판사)
else:
    print("Error Code:" + rescode)

print()

url = "https://openapi.naver.com/v1/search/shop.json"
option = "&display=1&sort=count"
query = "?query="+urllib.parse.quote(input("검색 : "))
url_query = url + query + option
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    res = response_body.decode('utf-8')

    jsonres = json.loads(res)

    result = []

    for i in jsonres['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        메이커 = re.sub('<.+?>', '', i['maker'], 0, re.I | re.S)
        브랜드 = re.sub('<.+?>', '', i['brand'], 0, re.I | re.S)
        print(타이틀+"|"+메이커+"|"+브랜드)
else:
    print("Error Code:" + rescode)