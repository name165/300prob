def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade) #리스트 길이 저장
    count = 0
    for i in range(arr_length): #리스트 돌기
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10: # 80 이상 석차 10% 이내
            count += 1  #count 1 증가
        elif current_grade[i] >= 80 and rank[i] == 1: # 80 이상 1등
            count += 1 # count 1 증가
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]: #점수가 가장 많이 올랐을 경우
            count += 1 # count 1 증가
    return count # count 반환

def func_b(current_grade):
    arr_length = len(current_grade) # 리스트 길이 저장
    rank = [1] * arr_length #rank 리스트에 current_grade 리스트 길이 만큼 항목 생성
    for i in range(arr_length): # 비교값 a
        for j in range(arr_length): #비교값 b
            if current_grade[i] < current_grade[j]: # a가 b보다 작을때
                rank[i] += 1 #a의 순위 1 증가
    return rank #순위 반환

def func_c(current_grade, last_grade):
    max_diff_grade = 1 #증가한 점수
    for i in range(len(current_grade)): #current_grade 리스트 항목 수 만큼 반복
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i]) #현재 점수 - 과거 점수, 1중 최댓값을 저장
    return max_diff_grade # 증가한 점수 반환

def solution(current_grade, last_grade):
    rank = func_b(current_grade) # 순위 저장
    max_diff_grade = func_c(current_grade, last_grade) # 증가한 점수 최댓값
    answer = func_a(current_grade, last_grade, rank, max_diff_grade) #count 반환
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#1.성적이 80점 이상이며 10% 이내이거나 1등인 학생 혹은 직전 학기 대비 성적이 가장 많이 오른 학생이 몇명인지 구함
#2.func_b:각 학생별 석차 구하기
#2-2.func_c:직전 학기 대비 오른 성적 구하기
#2-3.장학생 수 구하기
#3.