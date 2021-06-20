def solution(papers, K):
    length = len(papers)
    for i, paper in enumerate(papers): # 사람 번호와 필요한 종이 수
        K -= paper # 현재 종이 수에서 필요한 만큼의 종이 수를 뺌
        if K < 0: # 종이가 부족하면
            length = i - 1 # 현재 번호를 저장
    return length

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
papers1 = [2, 4, 2, 3, 1]
K1 = 10
ret1 = solution(papers1, K1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

papers2 = [2, 4, 2, 3, 1]
K2 = 14
ret2 = solution(papers2, K2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")