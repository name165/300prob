#문제8

def solution( sentence ):
    str = ''
    for c in sentence: # 문장 한 글자씩 가져오기
        if c != '.' and c != ' ': # . 혹은 공백일시 스킵
            str += c
    size = len(str)
    for i in range(size//2):
        if str[i] != str[size -1 - i]:
            return False
    return True

s1 = "never odd or even"
ret1 = solution( s1 )
print("solution 함수의 결과 :", ret1)

s2 = "palindrome"
ret2 = solution( s2 )
print("solution 함수의 결과 :", ret2)