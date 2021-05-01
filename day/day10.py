# 함수 : 상자 안에 들어있는 수 => 미리 정의된 수
    # 함수 형태 : 인수 => 정의 => 반환

# 복습 : 입력을 입력받아 입력을 반환
    #나이를 입력받아 나이를 반환

def 이름():
    이름 = input("이름 입력 : ")
    return 이름

def 나이():
    나이 = input("나이 입력 : ")
    return 나이

print(이름())
print(나이())
#복습2: 세개의 수를 입력받아 함수에 전달
    #세개의 수중 가장 큰수 반환

def 최댓값(a, b, c):
    list=[a,b,c]
    return max(list)

a=int(input())
b=int(input())
c=int(input())
print(최댓값(a,b,c))