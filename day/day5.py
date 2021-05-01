'''#문법 [명령어]
#출력: print()
#입력: input() / int(input())
#변수: 데이터 저장소

#산술연산자: +더하기 -뺴기 *곱하기 /나누기 //(나누기)몫 %(나누기)나머지
    # => 결과 => 값        2+2=>4
#비교연산자: >초과 <미만 >=이상 <=이하 ==같다 !=같지 않다
    # => 결과 => T[참] F[거짓]   2>=1 => T

#관계연산자:
#           and : 이면서 면서 그리도 모두 80~90 초콜릿이면서사탕// 조건 모두 T => T
                #10>=5 and 10<=20
#           or : 이거나 거나 하나라도          초콜릿이거나사탕//조건 하나라도 T=> T
                #10>=5 or 10<=20
#          not : 반대[부정] True[참] => False[거짓]

#복합대입연산자 : 계산후에 대입 기호
    # 변수 = 변수 + 값 // 변수 += 값
    # 변수 = 변수 - 값 // 변수 -= 값
    # 변수 = 변수 * 값 // 변수 *= 값
    # 변수 = 변수 / 값 // 변수 /= 값
    # 변수 = 변수 % 값 // 변수 %= 값
    # 변수 = 변수 // 값 // 변수 //= 값

#반복문: while for

# while

# while 논리 : # 논리가 T[참이면] 반복 실행 F[거짓이면] 반복중단

#예1) 5회 반복
반복 =0
while 반복<5:
    print("반복중")
    반복 += 1

#예2> 1~100 까지 누적 합계
합계 = 0
수 = 1
while 수 <=100:
    합계+=수
    수+=1

print(합계)


#for 변수 in range(시작, 끝): # 시작부터 끝까지 1씩 증가하면서 변수에 대입, 끝값에서 반복 중단

#예1> 5회 반복
for 반복 in range(5):
    print("for 반복중")



#제어문[판단] : if
#   if 논리:
#       참
#   else:
#       거짓
###############################################################################
#여러개 판단하기
#if 논리:
#   참
#elif 논리2:
#   참2
#elif 논리3:
#   참3
#else:
#   거짓

import random

if 10>=5:
    print("[T자리]")
else:
    print("[F자리]")
#문제1
score = int(input())
if score>=80:
    print("합격")
else:
    print("불합격")
#문제2
    score1=int(input())
    if score1>=90:
        print("최우수")
    elif score1>=80:
        print("우수")
    elif score1>=70:
        print("보통")
    else:
        print("미달")
#문제3
    sc=list(map(int, input().split()))
    max=0
    for i in sc:
        if i>max:
            max=i
    print(max)

#문제4
    p1 = int(input())
    p2 = int(input())
if p1 == 0:
    if p2 == 1:
        print("p1 승")
    elif p2 == 1:
        print('p2 승')
    else:
        print("무승부")
if p1 == 1:
    if p2 == 0:
        print("p1 승")
    elif p2 == 2:
        print('p2 승')
    else:
        print("무승부")
if p1 == 2:
    if p2 == 1:
        print("p1 승")
    elif p2 == 0:
        print('p2 승')
    else:
        print("무승부")

p1w = 0
while True:
    p1 = int(input()) # 가위(0), 바위(1), 보(2) 선택
    p2 = random.randint(0, 2) # 0~2까지 난수 생성
    print(p2, p1w)
    if p1 == 4:
        break
    if p1 == 0: # p1이 가위(0) 일때
        if p2 == 2: #p2이 보(2) 일때
            print("p1 승") #p1 승
            p1w += 1 # pw2+1
        elif p2 == 1: #p2이 바위(1) 일때
            print('p2 승') #p2 승
            p1w -= 1 # p1w-1
        else:
            print("무승부") #p2이 가위(0) 면 무승부
    if p1 == 1: #p1이 바위(1)일때
        if p2 == 0: #p2이 가위(0)일때
            print("p1 승") #p1 승
            p1w += 1 # p1w+1
        elif p2 == 2: #p2이 보(2)일때
            print('p2 승') #p2 승
            p1w -= 1 # p1w-1
        else:
            print("무승부") #p2이 바위(1) 면 무승부
    if p1 == 2: #p1이 보(2)일때
        if p2 == 1: #p2이 바위(1)일때
            print("p1 승") #p1 승
            p1w += 1 # p1w+1
        elif p2 == 0: #p2이 가위(0) 일때
            print('p2 승') #p2 승
            p1w -= 1 # p1w-1
        else:
            print("무승부") #p2이 보(2) 면 무승부

if p1w>0: #만약 p1w가 0보다 크다면
    print("p1 승")
elif p1w<0:#만약 p1w가 0보다 작다면
    print("p2 승")
else: #p1w가 0이면
    print("무승부")'''

for 곱 in range(1,10):
    print("2 *", 곱, "=", 2*곱)

단=int(input())
for 곱 in range(1,10):
    print(단, "*", 곱, "=", 단*곱)

for 단 in range(2,11):
    print(단, '단')
    for 곱 in range(1,10):
        print(단, "*", 곱, "=", 단*곱)

for i in range(5):
    for j in range(5-i):
        print(" ", end='')
    for k in range(i+1):
        print("*", end='')
    print("")


