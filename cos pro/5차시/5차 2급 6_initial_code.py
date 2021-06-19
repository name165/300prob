def solution(korean, english):
    answer = 0
    math = 210 - (korean + english) # 평균 70일때 총좀 = 70 * 3 = 210, 210 - (국어 점수 + 영어 점수) = 수학 점수
    if math > 100: #수학 점수가 100점 초과
        answer = -1 #불가능
    else: # 100점 이하
        answer = math # 수학 점수
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
korean = 70
english = 60
ret = solution(korean, english)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")