def solution(password):
    capital_count, small_count, digit_count = 0, 0, 0
    for p in password:
        if p >= 'A' and p <= 'Z': # 문자가 대문자 알파벳
            capital_count += 1
        elif p >= 'a' and p <= 'z': # 문자가 소문자 알파벳
            small_count += 1
        elif p >= '0' and p <= '9': # 문자가 숫자
            digit_count += 1
    if capital_count > 0 and small_count > 0 and digit_count > 0: # 모두 만족할때
        answer = True # 참
    else:
        answer = False # 거짓
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
password1 = "helloworld"
ret1 = solution(password1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "Hello123"
ret2 = solution(password2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")