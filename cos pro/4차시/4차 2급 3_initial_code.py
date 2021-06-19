def func_a(bundle, start):# 카드 뽑아오기
    return bundle[start::2]

def func_b(score1, score2): #점수 비교
    if score1 > score2: #1번 승
        return [1, score1]
    elif score2 > score1: #2번 승
        return [2, score2]
    else: #무승부
        return [0, score1]

def func_c(bundle): # 점수 구함
    answer = 0
    score_per_cards = { #문자별 점수
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle: # 카드 문자 가져오기
        answer += score_per_cards[card] # 문자별 점수 증가
    return answer
        
def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n] #1번 카드 가져오기(홀수번째)
    b_cards = func_a(bundle, 1)[:n] #2번 카드 가져오기(짝수번째)
    a_score = func_c(a_cards) #1번 점수 구하기
    b_score = func_c(b_cards) #2번 점수 구하기
    return func_b(a_score, b_score ) # 점수 비교

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")