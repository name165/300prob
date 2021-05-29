def solution(num):
    count = 0
    for i in range(1,num+1):
        current = i
        while current != 0:
            if current % 10 in [3, 6, 9]:
                count += 1
            current //= 10
    return count

print(solution(40))