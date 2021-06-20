#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    #여기에 코드를 작성해주세요.
    answer = [0 for _ in range(4)]
    for s in people: # 사람 사이즈 가져오기
        if s<95: answer[0] += 1 # 95 미만 : S
        elif s<100: answer[1] += 1 # 95 이상 100 미만 : M
        elif s<105: answer[2] += 1 # 100 이상 105 미만 : L
        else: answer[3] += 1 # 105 이상 : XL
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")