#문제6

def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1, len(floors)):
        if floors[i]>floors[i-1]:
            dist += floors[i] - floors[i - 1]
        else:
            dist += floors[i - 1] - floors[i]
    return dist

floors = [1, 2, 5, 4, 2]
ret = solution(floors)

print(ret)