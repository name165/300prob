#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0
    for c in cards: # 카드 가져오기
        answer += int(c[1]) # 카드 숫자 합 저장
    if cards[0][0] == cards[1][0] and cards[1][0] == cards[2][0] : return answer * 3 # 모든 카드의 색깔이 같을 시 카드 숫자 합 * 3 반환
    elif cards[0][0] != cards[1][0] and cards[1][0] != cards[2][0]: return answer # 모든 카드의 색깔이 다를 시 카드 숫자 합 반환
    else: return answer * 2 # 카드 2장의 색이 같을시 카드 숫자 합 * 2 반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")