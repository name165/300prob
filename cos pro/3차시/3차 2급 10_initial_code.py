def solution(arr):
    answer = 0
    for i in arr: # arr 리스트 값 가져오기
        if i/2 in arr: # 자신을 2로 나눈 값이 arr 리스트 안에 있다면
            answer += 1 # answer 1 증가
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
arr = [4, 8, 3, 6, 7]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")