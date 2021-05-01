#111
text = input()
print(text*2)

#112
a = input()
print(int(a)+10)

#113
a=int(input())
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
a = int(input("입력값: "))
if a + 20 > 255:
    print("출력값: 255")
else:
    print("출력값:", a+20)

#115
a = int(input("입력값: "))
if a - 20 > 255:
    print("출력값: 255")
elif a - 20 < 0:
    print("출력값: 0")
else:
    print("출력값:", a+20)

#116
time = input()
time1 = time.split(":")
if time1[1] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")

#117
fruit = ["사과", "포도", "홍시"]
fruit1= input("좋아하는 과일은? ")
if fruit1 in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
inv = input()
if inv in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

#119
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
fr = input("제가 좋아하는 계절은: ")
if fr in fruit.keys():
    print("정답입니다")
else:
    print("오답입니다")

#120
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
fr = input("좋아하는 과일은? ")
if fr in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")

#121
a=input()
if a.islower() is True:
    print(a.upper())

elif a.isupper() is True:
    print(a.lower())

#122
score = int(input())
if 81 <= score and score <= 100:
    print("grade is A")
elif 61 <= score and score <= 80:
    print("grade is B")
elif 41 <= score and score <= 60:
    print("grade is C")
elif 21 <= score and score <= 40:
    print("grade is D")
elif 0 <= score and score <= 20:
    print("grade is E")

#123
money = input().split()
result = 0
if money[1] == "달러":
    result = int(money[0]) * 1167
elif money[1] == "엔":
    result = int(money[0]) * 10.96
elif money[1] == "유로":
    result = int(money[0]) * 1268
elif money[1] == "위안":
    result = int(money[0]) * 171
print(result, "원")

#124
num1 = int(input("input number1: "))
max = num1
num2 = int(input("input number2: "))
if num2 > max:
    max = num2
num3= int(input("input number3: "))
if num3 > max:
    max = num3
print(max)

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