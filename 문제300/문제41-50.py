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