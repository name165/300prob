#171
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])
print("-----------")

#172
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])
print("-----------")

#173
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(3-i, price_list[i])
print("-----------")

#174
price_list = [32100, 32150, 32000, 32500]
for i in range(3):
    print(100+10*i, price_list[i])
print("-----------")

#175
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i],my_list[i+1])
print("-----------")

#176
my_list = ["가", "나", "다", "라","마"]
for i in range(3):
    print(my_list[i],my_list[i+1],my_list[i+2])
print("-----------")

#177
my_list = ["가", "나", "다", "라"]
for i in range(3,0,-1):
    print(my_list[i],my_list[i-1])
print("-----------")

#178
list = [100,200,400,800]
for i in range(3):
    print(list[i+1]-list[i])
print("-----------")

#179
list = [100,200,400,800,1000,1300]
for i in range(4):
    print((list[i]+list[i+1]+list[i+2])/3)
print("-----------")

#180
low_price = [100, 200, 400, 800, 1000]
high_price = [150,300,430,880,1000]
volatility = []
for i in range(5):
    volatility.append(high_price[i]-low_price[i])
print(volatility)
print("-----------")