#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 64
    x=[]
    y=[]
    for i in bishops:
        x=ord(i[0])-64
        y=int(i[1])
        answer -= min(x, y)
        answer -= min(8 - x, y)
        answer -= min(x, 8 - y)
        answer -= min(8 - x, 8 - y)
    print(x,y)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")