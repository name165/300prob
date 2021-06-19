def solution(classes, m):
    answer = 0
    for students in classes: # 학생 수 가져오기
        answer += students // m # 학생수를 조교 수로 나눈 값
        if students % m != 0: # 학생수를 조교 수로 나눈 나머지가 0이 아님(남는 학생이 있음)
            answer += 1 # 1 증가
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")