def solution(programs):
    answer = 0
    used_tv = [0] * 25 # tv 사용 시간 24시간(0 제외)

    for program in programs: #tv 시청 시간
        for i in range(program[0], program[1]): #시작시간부터 종료 시간까지
            used_tv[i] = used_tv[i] + 1 #1 추가
    
    for i in used_tv:
        if i > 1: #시간안에 시청중인 프로그램이 1개 초과
            answer = answer + 1 # answer 1 증가
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")