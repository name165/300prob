#221
def print_reverse(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i],end='')
    print('')
print_reverse("python")

#222
def print_score(a):
    print(sum(a)/len(a))
print_score([1,2,3])
#223
def print_even(a):
    for i in a:
        if i%2==0:
            print(i)
print_even([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(a):
    for i in a.keys():
        print(i)
print_keys({"이름":"김말똥","나이":30,"성별":0})

#225
my_dict = {"10/26":[100, 130, 100, 100],"10/27":[10,12,10,11]}
def print_value_by_key(dic,k):
    print(dic[k])
print_value_by_key(my_dict,"10/26")
#226
def print_5xn(a):
    i=0
    for i in range((len(a)//5)):
        for j in range(5):
            print(a[5*i+j],end='')
        print()
    for i in a[5*(i+1):]:
        print(i,end='')
    print()
print_5xn("1234567")
#227
def print_mxn(a,m):
    i=0
    for i in range((len(a)//m)):
        for j in range(m):
            print(a[m*i+j],end='')
        print()
    for i in a[m*(i+1):]:
        print(i,end='')
    print()
print_mxn("1234567",4)
#228
def calc_monthly_salary(annual_salary):
    print(annual_salary//12)
calc_monthly_salary(12000000)
#229
'''
왼쪽=100
오른쪽=200
'''
#230
'''
왼쪽=100
오른쪽=200
'''