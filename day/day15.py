import pygame # pygame 파일 가져오기 => pygame 관련 함수 사용 가능
import sys # sys 파일 가져오기 => sys 관련 함수 사용 가능
from pygame.locals import *

pygame.init() #게임 초기화
display = pygame.display.set_mode( (640, 960) )
pygame.display.set_caption("벽돌 깨기") # 게임 제목
time = pygame.time.Clock() # 초당 동작 수
pygame.key.set_repeat(1, 1)

#함수 : 미리 작성된 코드
#벽돌 그리기 함수
def brickdraw():
    for 벽돌 in 벽돌리스트:
        pygame.draw.rect(display, ( 0 , 211, 149) , 벽돌)
            #draw = 그리기,rect = 사각형
                #위치 , 색상 , 크기(x축 크기, y축 크기, x축 위치, y축 넓이)

#공 그리기함수
def ball():
    pygame.draw.circle(display, (255, 255, 0), (int(x), int(y)), 20)

font1 = pygame.font.SysFont(None, 60)
score = 0
x = int(640/2) # 가로 화면 크기
y = 960 - 20
dx = 10# 오른쪽
dy = 10 #아래로

#페달 변수
페달세로 = 20 #페달 세로 크기
페달가로 = 150 #페달 가로 크기
페달x = (640 - 페달가로) / 2
페달 = pygame.Rect(페달x, 960 - 페달세로 - 20, 페달가로, 페달세로)

#벽돌 변수
벽돌리스트= [ ]
for 열 in range(7):  #세로 6회
    for 행 in range(10):  #가로 10회
        벽돌 = pygame.Rect(열*(60+15)+70, 행*(32+20)+48, 70, 32)
        벽돌리스트.append(벽돌) # 벽돌 리스트에 추가

def drawpedal():
    pygame.draw.rect(display, (0, 211, 149), 페달)

while True:
    #공 이동
    x += dx #x축 + 0.1
    y += dy #y축 - 0.1
    #background = pygame.image.load("backg.jpg")
    #display.blit(background, (0, 0))
    display.fill("blue")

    #공 벽 충돌 검사
    if x + dx > 640 - 7 or x+dx < 7: #화면 최대 가로 480 - 7[여백]
        dx = -dx    #화면 최대 가로 크기 보다 커지면 방향 전환
    if y + dy < 7: # 화면 최대 세로 320 - 7[여백]
        dy = -dy    #화면 최대 세로 크기 보다 커지면 방향 전환
    elif ( y + dy > 930): # 공 세로축이 바닥에 닿음
        if x > 페달x and x < 페달x + 페달가로: # 페달에 공이 닿으면
            dy = -dy # 방향 전환
        else:
            pygame.quit()
            sys.exit()
    #벽돌 충돌 검사
    for 벽돌 in 벽돌리스트:
        if x > 벽돌.x and x < 벽돌.x + 벽돌.width and y>벽돌.y and y<벽돌.y+벽돌.height:
            dy = -dy #방향 전환
            벽돌리스트.remove(벽돌) # 벽돌 제거
            score += 1

    #동작
    for event in pygame.event.get() : #이벤트 = 동작
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN : # 키보드 입력
            if event.key == pygame.K_LEFT : #왼쪽 키 입력
                페달.left -= 1
                페달x -= 1
            elif event.key == pygame.K_RIGHT: #오른쪽 키 입력
                페달.left += 1
                페달x += 1

    #그리기
    brickdraw()
    ball()
    drawpedal()
    img1 = font1.render(str(score), True, 'white')
    display.blit(img1, (50, 50))

    #게임 업데이트
    pygame.display.update()
    time.tick(30)

