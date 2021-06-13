def solution(member_age, transportation):
	if transportation == 'Bus': # 버스 이용 시
		adult_expense = 40000 # 어른 가격 30000원
		child_expense = 15000 # 어린이 가격 15000원
	elif transportation == 'Ship': # 배 이용시
		adult_expense = 30000 # 어른 가격 30000원
		child_expense = 13000 # 어린이 가격 13000원
	elif transportation == 'Airplane': # 비행기 이용시
		adult_expense = 70000 # 어른 가격 70000원
		child_expense = 45000 # 어린이 가격 45000원

	if len(member_age) >= 10: # 인원수 10 명 이상
		adult_expense = int(adult_expense * 0.9) # 어른 10% 할인
		child_expense = int(child_expense * 0.8) # 어린이 20% 할인

	total_expenses = 0
	for age in member_age: # 인원 나이 가져오기
		if age >= 20: # 어른일 시
			total_expenses += adult_expense # 성인 가격 추가
		else: # 어린이 일시
			total_expenses += child_expense # 어린이 가격 추가

	return total_expenses


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")