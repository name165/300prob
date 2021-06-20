def solution(money, chairs, desks):
    answer = 0
    for chair in chairs: # 의자 가격
        for desk in desks: # 책상 가격
            price = chair + desk #의자 가격 + 책상 가격
            if answer < price and price <= money: #가격이 현재 최댓값보다 크고 가진 돈보다 작거나 같을때
                answer = price # 최댓값을 현재 가격으로 저장
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money1 = 7
chairs1 = [2, 5]
desks1 = [4, 3, 5]
ret1 = solution(money1, chairs1, desks1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 7
chairs2 = [3]
desks2 = [5]
ret2 = solution(money2, chairs2, desks2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")