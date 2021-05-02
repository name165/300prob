#문제 1
print("Hello World")
#문제 2
print("Mary's cosmetics")
#문제 3
print('''신씨가 소리쳤다. "도둑이야".''')
#문제 4
print('"C:\\Windows')
#문제 5
print("안녕하세요.\n,만나서\t\t반갑습니다.")
#문제 6
print("오늘은", "일요일")
#문제 7
print("naver", "kakao", "sk", "samsumg", sep=";")
#문제 8
print("naver", "kakao", "sk", "samsumg", sep="/")
#문제 9
print("first ",end=''); print("second")
#문제 10
print(5/3)
#문제11
삼성전자=50000
print(10*삼성전자)
#문제12
시총=298
현재가=50000
per=15.78
print("항목\t\t값")
print("시가총액",시총)
print("현재가",현재가)
print("PER",per)
#문제13
s="hello"
t="python"
print(s+"! "+t)
#문제14
print(2 + 2 * 3)
#문제15
a="132"
print(type(a))
#문제16
num_str="720"
print(int(num_str))
#문제17
num=100
print(str(num))
#문제18
num_str = "15.79"
print(float(num_str))
#문제19
year = "2020"
print(int(year)-1, int(year)-2, int(year)-3)
#문제20
mon=48584
print(mon*36)
#문제21
letters = 'python'
print(letters[0], letters[2])
#문제22
license_plate= "24가 2210"
print(license_plate[4:8])
#문제23
string = "홀짝홀짝홀짝"
print(string[0::2])
#문제24
string = "PYTHON"
print(string[::-1])
#문제25
phone_number = "010-1111-2222"
print(phone_number[0:3], phone_number[4:8], phone_number[9:])
#문제26
print(phone_number[0:3], phone_number[4:8], phone_number[9:], sep="")
#문제27
url = "http://sharebook.kr"
print(url.split(".")[1])
#문제28
#문제29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)
#문제30
string = 'abcd'
string = string.replace('b', 'B')
print(string)
#문제31
a="3"
b="4"
print(a + b)
#문제32
print("Hi" * 3)
#문제33
print("-"*80)
#문제34
t1="python "
t2="java "
print((t1+t2)*4)
#문제35
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))
#문제36
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))
#문제37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
#문제38
상장주식수 = '5,969,782,550'
print(int(상장주식수.replace(",","")))
#문제39
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
#문제40
data = "  삼성전자   "
print(data.strip())
#문제41
ticker = "btc_krw"
print(ticker.upper())
#문제42
ticker = "BTC_KRW"
print(ticker.lower())
#문제43
str = 'hello'
print(str.capitalize())
#문제44
filename = "보고서.xlsx"
print(filename.endswith(".xlsx"))
#문제45
filename = "보고서.xls"
print(filename.endswith(("xlsx", "xls")))
#문제46
filename = "2020_보고서.xlsx"
print(filename.startswith("2020"))
#문제47
a = "hello world"
print(a.split())
#문제48
ticker = "btc_krw"
print(ticker.split("_"))
#문제49
date="2020-05-01"
print(date.split("-"))
#문제50
data="039490    "
print(data.rstrip())
#문제51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
#문제52
movie_rank.append("배트맨")
print(movie_rank)
#문제53
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
#문제54
movie_rank.remove("럭키")
print(movie_rank)
#문제55
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)
#문제56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
#문제57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max :", max(nums))
print("min :", min(nums))
#문제58
nums = [1, 2, 3, 4 ,5]
print(sum(nums))
#문제59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
#문제60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))
#문제61
price = ["20180728", 100, 130, 140, 150, 160, 170]
print(price[1:])
#문제62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
#문제63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
#문제64
nums = [1, 2, 3, 4, 5]
print(nums[4::-1])
#문제65
interest = ['삼성전자', "LG전자", "Naver"]
print(interest[0::2])
#문제66
interest = ['삼성전자', "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print(" ".join(interest))
#문제67
interest = ['삼성전자', "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print("/".join(interest))
#문제68
interest = ['삼성전자', "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print("\n".join(interest))
#문제69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)
#문제70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
#문제71
my_variable = ()
#문제72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
#문제73
tup = (1)
#문제74
#t = (1, 2, 3)
#t[0] = 'a'
#문제75
t= 1, 2, 3, 4
#int
#문제76
t = ('a', 'b', 'c')
t = ('A', "b", "c")
print(t)
#문제77
interest = ("삼성전자", "LG전자", "SK Hynix")
interest = list(interest)
print(interest)
#문제78
interest =["삼성전자", "LG전자", "SK Hynix"]
interest = tuple(interest)
print(interest)
#문제79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
#문제80
t = [i for i in range(2, 99, 2)]
t = tuple(t)
print(t)
#문제81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)
#문제82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)
#문제83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b  = scores
print(valid_score)
#문제84
temp = {}
#문제85
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)
#문제86
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)
#문제87
print("메로나 가격:", ice["메로나"])
print(ice)
#문제88
ice["메로나"] = 1300
print(ice)
#문제89
del(ice["메로나"])
print(ice)
#90
#누가바라는 key값에 대응되는 value값이 없음
#91
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)
#92
print(inventory["메로나"][0], "원")
#93
print(inventory["메로나"][1], "개")
#94
inventory['월드콘'] = [500, 7]
print(inventory)
#95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
lis = list(icecream.keys())
print(lis)
#96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
lis = list(icecream.values())
print(lis)
#97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
lis = list(icecream.values())
print(sum(lis))
#98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {"팥빙수": 2700, "아맛나": 1000}
icecream.update(new_product)
print(icecream)
#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
results = dict(zip(keys, vals))
print(results)
#100
data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
print(close_table)
#101
#Bool
#102
#False
#103
#True
#104
#True
#105
#True
#106
#비교에서 =>,=<는 사용불가
#107
#없음
#108
#Hi, there.
#109
#1 2 4
#110
#3 5
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
#121
a=input()
if a.islower():a = a.upper()
if a.isupper():a = a.lower()
print(a)
#122
score = int(input("score:"))
print("grade is")
if score<100 and score>80:print("A")
elif score>60:print("B")
elif score>40:print("C")
elif score>20:print("D")
elif score>0:print("E")
#123
money = input()
money = money.split(" ")
money[0] = int(money[0])
if money[1] == "달러": money[0] *= 1167
if money[1] == "위안": money[0] *= 1.096
if money[1] == "유로": money[0] *= 1268
if money[1] == "위안": money[0] *= 171
print(money[0], "원")
#124
n1 = input("input number1")
n2 = input("input number2")
n3 = input("input number3")
print(max([n1, n2, n3]))

#125
num=input().split("-")
if num[0] == "011":
    print("당신은 SKT 사용자입니다")
if num[0] == "016":
    print("당신은 KT 사용자입니다")
if num[0] == "019":
    print("당신은 LGU 사용자입니다")
if num[0] == "010":
    print("당신은 알수없는 사용자입니다")

#126
num = input("우편번호: ")
if num[2] in ["0", "1", "2"]:
    print("강북구")
elif num[2] in ["3", "4", "5"]:
    print("도봉구")
elif num[2] in ["6", "7", "8", "9"]:
     print("노원구")

#127
num= input("주민등록번호:")
back= num.split("-")[1]
if back[0] in ["1", "3"]:
    print("남자")
elif back[0] in ["0", "2"]:
    print("여자")

#128
num= input("주민등록번호:")
back= num.split("-")[1][1:3]
if 0 <= int(back) and int(back) <= 8:
    print("서울입니다")
else:
    print("서울이 아닙니다")

#129
num= input("주민등록번호:").split("-")
num1=num[0]+num[1][0:6]
al = 0
i = 0
while True:
    if i>=8:
        break
    al += int(num1[i]) * (i+2)
    i+=1
for i in range(4):
    al += int(num1[i+8]) * (i+2)
if (11 - al%11) == int(num[1][6]):
    print("유효한 주민등록번호 입니다")
if (11 - al%11) != int(num[1][6]):
    print("유효하지 않은 주민등록번호 입니다")

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
change = int(btc["max_price"]) - int(btc["min_price"])
if int(btc["opening_price"]) + change > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
