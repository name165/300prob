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