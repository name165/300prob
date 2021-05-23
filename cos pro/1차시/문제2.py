#문제 2
def solution(price, grade):
    if grade == "S":return price*0.95
    elif grade == "G":return price*0.9
    elif grade == "V":return price*0.85

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

print("solution : return value of the fuction is ", ret1)

price1 = 96900
grade1 = "S"
ret2 = solution(price1, grade1)
print("solution : return value of the fuction is ", ret2)