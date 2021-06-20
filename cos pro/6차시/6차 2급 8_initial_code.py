def func_a(number1, number2): # 두 수의 차 출력
    ret = 0
    if number1 > number2: # number1이 number2보다 크면
        ret = number1 - number2 # number1 - number2
    else: # 아니면
        ret = number2 - number1 # number2 - number1
    return ret

def func_b(number):
    ret = 0
    while number != 0: # 수가 0이 아닐때까지
        number = number // 10 # number를 10으로 나눈 몫으로 저장
        ret += 1 # 길이 1 증가
    return ret

def func_c(number, digit):
    ret = 0
    for i in range(digit): #길이 만큼 반복
        temp = number % 10 #10으로 나눈 나머지 ( 맨 뒤의 값 )
        number = number // 10 #10으로 나눈 몫
        ret = ret * 10 + temp # 현재 값에 10을 곱하고 맨 뒤의 값을 더함
    return ret

def solution(number):
    answer = 0
    digit = func_b(number) # 문자열 길이
    convert_number = func_c(number,digit) # 문자열 뒤집기
    answer = func_a(number, convert_number) # 차 구하기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 120
ret1 = solution(number1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 23
ret2 = solution(number2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 깂은", ret2, "입니다.")