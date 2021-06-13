def func_a(scores, score):
    rank = 1 # 순위
    for s in scores: #scores 리스트 차례로 불러오기
        if s == score: #score와 일치할때
            return rank #rank(순위) 반환
        rank += 1 # 다음 등수
    return 0

def func_b(arr):
    arr.sort(reverse=True) #내림차순 정렬

def func_c(arr, n):
    return arr[n] # n 번째 값 반환

def solution(scores, n):
    score = func_c(scores, n) #n번 학생 점수 찾기
    func_b(scores) #scores 등수 순으로 정렬
    answer = func_a(scores, score) #n번 학생의 점수가 몇등인지 찾기
    return answer # answer 반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#1.n번 학생의 등수
#2-1.func_c : n번 학생의 점수 구하기
#2-2.func_b : scores 리스트 정렬
#2-3.func_a : 점수 검색
#3-1.시험 점수가 번호순으로 든 리스트:scores
#3-2.학번 : n


