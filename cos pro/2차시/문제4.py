#문제4
import math
def solution(words):
    answer = ''
    for i in words:
        if len(i)>=5:
            answer+=i
    if answer == '':
        answer = 'empty'
    return answer

words1 = ['my','favorite','color','is','violet']
ret1 = solution(words1)

print(ret1)

words2 = ['yes','i','am']
ret2= solution(words2)

print(ret2)