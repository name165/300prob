#201
def print_coin():
    print("비트코인")

#202
print_coin()

print()

#203
for i in range(100):
    print_coin()

#204
def print_coins():
    for i in range(100):
        print_coin


print()

#215
def print_with_smile(문자열):
    print(문자열 + ":D")

#216
print_with_smile("안녕하세요")

print()

#217
def print_upper_price(현재가):
    print(현재가*13//10)

print_upper_price(10000)
print()

#218
def print_sum(a,b):
    print(a+b)

print_sum(2,5)
print()

#219
def print_arithmetic_operation(a,b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmetic_operation(3,4)
print()

#220
def print_max(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)

print_max(9,7,6)
print()

#221
def print_reverse(문자열):
    for i in 문자열[len(문자열)::-1]:
        print(i,end='')
    print("\n")

print_reverse("python")

#222
def print_score(성적):
    print(sum(성적)/len(성적))

print_score([1,2,3])
print()

#223
def print_even(리스트):
    for i in 리스트:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])
print()

#224
def print_keys(딕셔너리):
    for i in 딕셔너리.keys():
        print(i)

print_keys({"이름":"김말똥", "나이":30, "성별":0})
print()

#225
def print_value_by_key(my_dict,key):
    print(my_dict[key])

my_dict = {"10/26":[100, 130, 100, 100], "10/27":[10,12,10,11]}
print_value_by_key(my_dict, "10/26")
print()

#226
def print_5xn(문자열):
    for i in range(len(문자열)):
        print(문자열[i],end='')
        if i%5==4:
            print()

print_5xn("아이엠어보이유알어걸")
print()

#227
def print_mxn(문자열,m):
    for i in range(len(문자열)):
        print(문자열[i],end='')
        if i%m==m-1:
            print()

print_mxn("아이엠어보이유알어걸",3)
print("\n")

#228
def calc_monthly_salary(annual_salary):
    print(annual_salary//12)

calc_monthly_salary(12000000)
print()

#232
def make_url(문자열):
    print("www."+문자열+".com")
make_url("naver")
print()

#233
def make_list(문자열):
    list=[]
    for i in 문자열:
        list.append(i)
    print(list)
make_list("abcd")
print()

#234
def pickup_even(list):
    ret = []
    for i in list:
        if i % 2 == 0:
            ret.append(i)
    print(ret)

pickup_even([3, 4, 5, 6, 7, 8])
print()

#235
def convert_int(num):
    ret = 0
    for i in num:
        if i!=',':
            ret *= 10
            ret += int(i)
    print(ret)

convert_int("1,234,567")
print()

import datetime
#241
print(datetime.datetime.today())
print()

#242
print(type(datetime.datetime.now()))
print()

import time

#243
for i in range(5, 0, -1):
    d = datetime.datetime.today() - datetime.timedelta(days=i)
    print(d.year, end='-')
    print(d.month, end='-')
    print(d.day)

print()

#244
d = time.localtime(time.time())
print(time.strftime("%H:%M:%S",d))

print()

#245
d = datetime.datetime.strptime("2020-05-04", "%Y-%m-%d")
print(d)
print()

#246
#while True:
#   d = time.localtime(time.time())
#   print(time.strftime("%H:%M:%S", d))
#   time.sleep(1)

import os

#248
print(os.getcwd())

#249
os.chdir("C:\\Users\\User\\Desktop")
os.rename("ㅎㅇ1.txt", "ㅎㅇ.txt")

print()

import numpy
#250
a=numpy.arange(0.0, 5.1, 0.1)
for i in a:
    print("%.1f" % i,end=' ')
