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
fluc = int(btc["max_price"])-int(btc["min_price"])
if int(btc["opening_price"])+fluc > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
