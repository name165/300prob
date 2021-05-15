#141
list = [100, 200, 300]
for i in list:
    print(i + 10)
print("-----------")

#142
list = ["김밥", "라면", "튀김"]
for i in list:
    print("오늘의 메뉴: ", i)
print("-----------")

#143
list = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list:
    print(len(i))
print("-----------")

#144
list = ["dog", "cat", "parrot"]
for i in list:
    print(i,len(i))
print("-----------")

#145
list = ["dog", "cat", "parrot"]
for i in list:
    print(i[0])
print("-----------")

#146
list = [1,2,3]
for i in list:
    print("3 x",i)
print("-----------")

#147
list = [1,2,3]
for i in list:
    print("3 x",i,"=",i*3)
print("-----------")

#148
list = ['가', '나', '다', '라']
for i in list[::2]:
    print(i)
print("-----------")

#149
list = ['가', '나', '다', '라']
for i in list[1:]:
    print(i)
print("-----------")

#150
list = ['가', '나', '다', '라']
for i in list[::-1]:
    print(i)
print("-----------")