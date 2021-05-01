import turtle

t=turtle.Turtle()
t.shape("turtle")
t.color("red")
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)

for i in range(4):
    t.forward(200)
    t.left(-90)
t.left(45)
t.forward(140)
t.left(-90)
t.forward(140)

t.circle(30)
t.left(-90)
t.forward(30)
t.left(45)
t.forward(30)
t.left(180)
t.forward(30)
t.left(90)
t.forward(30)
t.left(180)
t.forward(30)
t.left(-135)
t.forward(40)
t.left(45)
t.forward(30)
t.left(180)
t.forward(30)
t.left(90)
t.forward(30)
t.left(180)

# t.forward(360)
# t.left(90)
# t.forward(90)
# t.left(90)
# t.forward(90)
# t.left(-90)
# t.forward(90)
# t.left(90)
# t.forward(180)
# t.left(90)
# t.forward(90)
# t.left(-90)
# t.forward(90)
# t.left(90)
# t.forward(90)
# t.left(90)
# t.forward(90)
# t.circle(-45)
# t.forward(180)
# t.circle(-45)

colors = ["red" , "purple" , "blue" , "green" , "yellow" , "orange"]

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 1

while length < 300:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(59)
    length+=1

turtle.mainloop()

숫자상자 = 10
문자상자 = '파이썬'

print("숫자상자[변수]의 내용물 ??? : ",숫자상자)
print("문자상자[변수]의 내용물 ??? : ",문자상자)

숫자상자 = 20

print("숫자상자의 변경 후 내용물 ??? : ",숫자상자)

숫자상자2=숫자상자 + 10
print("숫자상자2의 계산후 내용물 ??? : ",숫자상자2)

print("\n")

금액=456789
print(" 십만원 ",금액//100000,"장")

금액=금액 - (금액//100000) * 100000
print(" 만원 ",금액//10000,"장")

금액=금액 - (금액//10000) * 10000
print(" 천원 ",금액//1000,"장")

금액=금액 - (금액//1000) * 1000
print(" 백원 ",금액//100,"개")

숫자= 32
print("현재 숫자변수는 2의 배수 확인 " , 숫자%2==0)
print("현재 숫자변수는 5의 배수 확인 " , 숫자%5==0)

