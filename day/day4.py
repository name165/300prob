#입출력
    #1.출력 print(출력 데이터)
    #2.입력 input()

#1 입력
input("이름을 입력:")

#2 입력받고 입력받은 값을 변수에 저장
이름=input("두번째 이름을 입력:")

#3 입력값 출력
print("첫번째 이름: ", )
print("두번째 이름: ", 이름 )
print("세번째 이름: ", input("세번째 이름 입력:"))

색상=input("원의 색상 입력:")
반지름=int(input("원 반지름 입력:"))

import turtle
t=turtle.Turtle()

t.shape("turtle")
t.color(색상)
t.begin_fill()
t.circle(반지름)
t.end_fill()

turtle.mainloop()

#입력받은 금액의 지폐수 세기
money = int(input("금액 입력:"))
print("입력한 금액은 :", type(money))
지폐=int(input("금액 입력:"))
print("입력한 지폐는 : ", type(지폐))

print("십만원 : ", 지폐//100000, "장")
지폐= 지폐%100000

print("만원권 : ", 지폐// 10000, "장")
지폐= 지폐%10000

print("천원권 : ", (지폐-(지폐//10000)*10000) // 1000, "장")

a=int(input())
print(a%2==0)


a_name=input("이름: ")
a_kor=int(input("국어 점수: "))
a_eng=int(input("영어 점수: "))
b_name=input("이름: ")
b_kor=int(input("국어 점수: "))
b_eng=int(input("영어 점수:"))
print("="*10+'점수'+"="*10)
print("성명 \t국어|영어|평균")
print(a_name, " ", a_kor, "", a_eng, "", (a_kor+a_eng)/2)
print(b_name, " ", b_kor, "", b_eng, "", (b_kor+b_eng)/2)

a_

# import turtle
# import random
#
# 플레이어=turtle.Turtle()
# 플레이어.color("blue")
# 플레이어.shape('turtle')
# 플레이어.penup()
# 플레이어.speed(0)
# screen=플레이어.getscreen()
#
# def 왼쪽회전():
#     플레이어.left(30)
#
# def 오른쪽회전():
#     플레이어.right(30)
#
# def 전진():
#     플레이어.forward((20))
#
# screen.onkeypress(왼쪽회전, "Left")
# screen.onkeypress(오른쪽회전, "Right")
# screen.onkeypress(전진, "Up")
# screen.listen()
#
# def 플레이():
#     플레이어.forward(2)
#
#     for a in asteroid:
#         a.right(random.randint(-180,180))
#         a.forward(2)
#
#         if 플레이어.distance(a)<20:
#             플레이어.write("game clear")
#             a.ht()
#
#     screen.ontimer(플레이, 10)
#
# screen.ontimer(플레이,10)
#
# asteroid=[]
#
# for i in range(10):
#     a1=turtle.Turtle()
#     a1.color("red")
#     a1.shape("circle")
#     a1.penup()
#     a1.speed()
#     a1.goto(random.randint(-300, 300), random.randint(-300, 300))
#     asteroid.append(a1)
#
# turtle.mainloop()