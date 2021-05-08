import pygame #파이게임 임포트
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN
                          #종료,직각,키 종료,위,왼쪽,오른쪽,아래
##########################################################################################
import random # 랜덤 파일 임포트
import sys # 시스템 파일 임포트

#2. 게임 설정
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
frame = pygame.time.Clock()

food = [] #음식 위치 저장
snake = [] #뱀 꼬리 위치 저장
(width, height) = (50, 50) # 가로 x 세로

#3.함수 만들기
#3-1. 음식 생성
def food_create():
    while True:
        pos = (random.randint(0, width-1), random.randint(0, height-1))
        if pos in food or pos is snake:
            continue
        food.append(pos)
        break
#3-2. 음식 이동
def food_move(pos):
    i = food.index(pos)
    del(food[i])
    food_create()
#3-3. 음식 그리기
def draw(message):
    global screen
    screen.fill((0, 0, 0))
    for f in food:
        pygame.draw.ellipse(screen, (0, 255, 0), Rect( (f[0])*30, (f[1])*30, 30, 30 ) )
    for body in snake:
        pygame.draw.rect(screen, (0, 255, 255), Rect(body[0]*30, body[1]*30, 30, 30))
    for index in range(34):
        pygame.draw.line(screen, (64, 64, 64), (index * 30, 0), (index * 30, 1000))
        pygame.draw.line(screen, (64, 64, 64), (0, index * 30), (1000, index * 30))
    if message != None:
        screen.blit(message, (500, 500))
    pygame.display.update()

#4.게임 실행

myfont = pygame.font.SysFont(None, 80)
key = K_DOWN
message = None
gameover = False
snake.append( (int(width/2), int(height/2)) )
for i in range(10):
    food_create()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key = event.key
    if not gameover:
        if key == K_LEFT:
            head = (snake[0][0] - 1, snake[0][1])
        elif key == K_RIGHT:
            head = (snake[0][0] + 1, snake[0][1])
        elif key == K_UP:
            head = (snake[0][0], snake[0][1] - 1)
        elif key == K_DOWN:
            head = (snake[0][0], snake[0][1] + 1)
        if head in snake or head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            message = myfont.render("Game over", True, (255, 255, 0))
            gameover = True
        snake.insert(0, head)
        if head in food:
            food_move(head)
        else:
            snake.pop()

    draw(message)
    frame.tick(5)