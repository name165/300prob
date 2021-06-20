def solution(money, price, n):
    answer = 0
    empty_bottle = answer = money // price # 빈병 : 현재 돈을 가격으로 나눈 몫
    while n <= empty_bottle: # 지금 가진 빈 병이 교환 가능한 병보다 많을 때
        empty_bottle = empty_bottle - n # 지금 가진 빈병에서 n개를 줌
        answer += 1
        empty_bottle += 1 # 빈 병이 한개 늘어남
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1, price1, n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 6
price2 = 2
n2 = 2
ret2 = solution(money2, price2, n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")