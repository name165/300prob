#문제3
def solution(m,n):
    answer = 0
    if m%2==1:m+=1
    for i in range(m,n,2):
        answer += i*i
    return answer

m = 4
n = 7

ret = solution(m,n)
print(ret)