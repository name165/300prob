def solution(sentence):
    res = ''
    for x in sentence:
        if x != ' ' or x != '.':
            res += x
    for i in range(len(res)//2):
        if res[i] != res[len(res)-i-1]:
            return False
    return True

    '''
    neverod doreven
    1234567 7654321
    '''


print(solution("never odd or even"))
print(solution("palindrome"))