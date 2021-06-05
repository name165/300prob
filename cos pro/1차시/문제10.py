def solution(data):
    cnt = 0
    total = sum(data)
    average = total / len(data)
    for d in data:
        if d < average:
            cnt += 1
    return cnt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)
print("solution 함수 결과 :",ret1)

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)
print("solution 함수 결과 :",ret2)
