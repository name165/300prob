#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(score):
	# 여기에 코드를 작성해주세요.
    answer = []
    rank = 1
    for i in score:
        for j in score:
            if i < j: # 리스트 내에 자신보다 큰 수가 있다면
                rank += 1 # 순위 하락
        answer.append(rank) # 답 리스트에 추가
        rank = 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")