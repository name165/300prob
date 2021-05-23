#문제4

def func_a(arr): #리스트 안의 자연수 개수 세기
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr): #가장 많이 들어있는 수의 개수
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr): # 가장 적게 들어있는 수의 개수
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("Solution: return value of solution is ", ret, ".")