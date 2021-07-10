# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    answer = ''
    cnt = 0
    while second > 14:
        second -= 14
        cnt += 1
    if cnt % 2 == 0: return "_" * (14 - second) + phrases[:second]
    else : return phrases[second:] + "_" * (14 - second)


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 20
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")