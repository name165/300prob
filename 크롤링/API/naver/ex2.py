#네이버 api 이용 json 가공 프로그램

import urllib.request
import sys
import os
import json
import re

def naversearch(cate,resnum):
    client_id = "o29ZhA_qIoynZire1FP4"
    client_secret = "cMjRJJ5Vl6"

    url = "https://openapi.naver.com/v1/search/"+cate+".json"
    option = "&display="+resnum+"&sort=count"
    query = "?query="+urllib.parse.quote(input( cate + "검색 :"))
    url_query = url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        검색결과 = response_body.decode('utf-8')

        json결과 = json.loads(검색결과)

        결과리스트 = []

        print("<----------검색 결과---------->")

        for i in json결과['items']:
            타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
            print(타이틀)

            if cate == 'shop':
                print("최저가 : ", i['lprice'] )

            if cate == 'movie':
                print("평점 : ", i['userRating'])

            if cate == 'book':
                print("작가 : ", i['author'])

            if cate == 'news' :
                print("주요내용 : ",i['description'])


while True:
    print("<----------검색 [naverAPI] 프로그램---------->")
    print("카테고리[ 1.뉴스 2. 쇼핑 3.도서 4.영화 5.사전], 0. 종료")
    op = int(input())

    if op == 1:
        cate = "news"
        resnum = input("출력 갯수")
        naversearch(cate, resnum)

    if op == 2:
        cate = "shop"
        resnum = input("출력 갯수")
        naversearch(cate, resnum)

    if op == 3:
        cate = "book"
        resnum = input("출력 갯수")
        naversearch(cate, resnum)

    if op == 4:
        cate = "movie"
        resnum = input("출력 갯수")
        naversearch(cate, resnum)

    if op == 5:
        cate = "encyc"
        resnum = input("출력 갯수")
        naversearch(cate, resnum)


    if op == 0:
        print("--이용해주셔서 감사합니다--")
        break