def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < num_carrot * 3: #사과가 당근의 3배 보다 많으면
        answer = num_apple // 3 # 만들수 있는 주스 양은 사과의 1/3

    else: # 아니라면
        answer = num_carrot # 만들수 있는 주스 양은 당근의 양

    num_apple -= answer * 3 # 주스를 만들때 사용한 사과 양을 사과에서 뺌 (남은 사과 양)
    num_carrot -= answer # 당근 양을 당근에서 뺌 (남은 당근 양)

    i = 0
    while k - (num_apple + num_carrot + i) > 0: # k에서 남은 사과 양과 당근 양 + i 를 뺌

        if i % 4 == 0: #i가 4의 배수라면
            answer -= 1 # 주스 양 - 1
        i = i + 1 # i를 더함
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")