#151
list = [3,-20,-3,44]
for i in list:
    if i<0:
        print(i)
print("-----------")

#152
list = [3, 100, 23, 44]
for i in list:
    if i%3==0:
        print(i)
print("-----------")

#153
list = [13, 21, 12, 14, 30, 18]
for i in list:
    if i%3==0 and i<20:
        print(i)
print("-----------")

#154
list = ['i', 'study', 'python', 'language', "!"]
for i in list:
    if len(i)>=3:
        print(i)
print("-----------")

#155
list = ["A", 'b', 'c','D']
for i in list:
    if i.isupper() == True:
        print(i)
print("-----------")

#156
list = ["A", 'b', 'c','D']
for i in list:
    if i.islower() == True:
        print(i)
print("-----------")

#157
list = ['dog','cat', 'parrot']
for i in list:
    print(i[0].upper() + i[1:])
print("-----------")

#158
list = ["hello.py", 'ex01.py', "intro.hwp"]
for i in list:
    print(i.split(".")[0])
print("-----------")

#159
list = ["intra.h", "intra.c", "define.h", "run.py"]
for i in list:
    if i.split(".")[1]=="h":
        print(i)
print("-----------")

#160
list= ["intra.h", "intra.c", "define.h", "run.py"]
for i in list:
    if i.split(".")[1]in ["h", "c"]  :
        print(i)
print("-----------")