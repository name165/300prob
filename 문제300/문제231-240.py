#231
#오류
#232
def make_url(n):
    return "www."+n+".com"
print(make_url("naver"))
#233
def make_list(a):
    li = []
    for i in a:
        li.append(i)
    return li
print(make_list('abcd'))
#234
def pickup_even(a):
    li = []
    for i in a:
        if i%2==0:
           li.append(i)
    return li
print(pickup_even([3,4,5,6,7,8]))
#235
def convert_int(a):
    li = ""
    for i in a:
        if i in '1234567890':
            li+=i
    return int(li)
print(convert_int("1,234,567"))
#236
#22

#237
#22

#238
#140

#239
#16

#240
#28