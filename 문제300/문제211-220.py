#211

#안녕
#Hi

#212

#7
#15

#213

#매개변수 문자열이 없음

#214
#문자열과 정수는 덧셈이 안됨

#215
def print_with_smile(a):
    print(a+":D")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(a):
    print(a*1.3)

#218
def print_sum(a,b):
    print(a+b)
#219
def print_arithmetic_operation(a, b):
    print(str(a) + " + " + str(b) + ' = ' + str(a + b))
    print(str(a) + " - " + str(b) + ' = ' + str(a - b))
    print(str(a) + " * " + str(b) + ' = ' + str(a * b))
    print(str(a) + " / " + str(b) + ' = ' + str(a / b))
print_arithmetic_operation(3,4)
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
