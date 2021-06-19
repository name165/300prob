def solution(point):
    if point < 1000: #만약 점수가 1000점 이하라면
        return 0 # 0 반환
    return point // 100 * 100 # 아닐 시 100으로 나눈 몫에 100을 곱해서 반환

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
point = 2323
ret = solution(point)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")