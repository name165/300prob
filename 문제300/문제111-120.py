#111
a=input()
print(a*2)
#112
a=int(input())
print(a+10)
#113
a=int(input())
if a%2==0:
    print("짝수")
else:print("홀수")
#114
a=int(input())
a+=20
if a>255:
    a=255
print(a)
#115
a=int(input())
a-=20
if a<0:
    a=0
print(a)
#116
a=input()
if(a.split(":")[1] == "00"):print("정각입니다")
else:print("정각이 아닙니다")
#117
fruit = ["사과", "포도", "홍시"]
a=input("좋아하는 과일은? ")
if a in fruit:print("정답입니다")
#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a=input()
if a in warn_investment_list:print("투자 경고 종목입니다")
else:print("투자 경고 종목이 아닙니다")
#119
fruit = {"봄":"딸기", "여름":"토마토", "가을": "사과"}
a = input("제가좋아하는계절은: ")
if a in fruit.keys():print("정답입니다")
else : print("오답입니다")
#120
fruit = {"봄":"딸기", "여름":"토마토", "가을": "사과"}
a = input("좋아하는과일은? ")
if a in fruit.values():print("정답입니다")
else : print("오답입니다")
