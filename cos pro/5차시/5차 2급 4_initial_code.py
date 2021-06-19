def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25: #태권도 25승 이상
    	answer += 250 #250점
    else: # 25승 미만
    	answer += taekwondo * 8 # 이긴 경기당 8점
    answer += 250 + (60 - running) * 5 # 달리기: 250점 + 빠른 시간 * 5 / 느린 시간 * -5
    count = 0
    for s in shooting:
    	answer += s # 맞춘 점수 추가
    	if s == 10: #10점 맞출시 count 증가
    		count += 1
    if count >= 7: # 7회 이상 10점 맞출시 100점 증가
    	answer += 100
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")