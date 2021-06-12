def solution(number):
    count = 0
    while number > 0 :
        n = number % 10
        if n in [2,3,5,7]:
            count += 1
        number //=10
    return count

number = 29022531
ret = solution(number)

print(ret)