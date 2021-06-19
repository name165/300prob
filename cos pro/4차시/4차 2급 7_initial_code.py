def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2): #이전 점수와 현재 점수 가져오기
        answer = max(answer, score2 - score1) # 현재 값과 현재점수 - 이전 점수 중 더 큰 값 저장
    return answer

def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2): #이전 점수와 현재 점수 가져오기
        answer = min(answer, score2 - score1)  # 현재 값과 현재점수 - 이전 점수 중 더 작은 값 저장
    return answer
            
def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores) # 점수 변화중 최댓값
    down = func_b(mid_scores, final_scores) # 점수 변화중 최솟값
    answer = [up, down] # 1, 2번 과정 값 리스트에 저장 후 반환
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")