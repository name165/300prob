def solution(schedule): # 상담 받지 못한 학생 수 구하기
    answer = [] # 상담 받지 못한 학생 리스트
    for idx, i in enumerate(schedule): #idx:리스트 요소 인덱스, i= 요소 값
        if i == "X": # i(요소값)가 X이면
            answer.append(idx+1) #학번 저장
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")