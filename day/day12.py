#1. 모듈 불러오기
import pygame #파이게임 모듈 가져오기
import random #난수 모듈 가져오기

#2.파이게임 기본 설정
pygame.init() #파이게임 초기화
width = 600 #화면 가로
height = 800 #화면 세로
display = pygame.display.set_mode( (width, height) )#화면 크기 설정
background = pygame.image.load("bg.jpg")
time = pygame.time.Clock() #시간 설정
point = 0 #초기 점수 설정
gameover = 0 # 끝 점수

#3.이미지 가져오기
dodge = pygame.image.load('missile.png')
charobj = pygame.image.load('fighter.png')

#pygame.mixer.music.load("bgm.mp3")
#pygame.mixer.music.play(-1)

#4. 미사일 여러개 랜덤 위치에 만들기
missile = []
for i in range(10):
    obj = pygame.Rect(dodge.get_rect()) # 이미지로 물체 그리기
    obj.left = random.randint(0, width)
    obj.top = -100
    speed =  random.randint(12, 15)
    missile.append( (obj, speed) ) #난수로 만들어진 물체와 속도를 리스트에 저장

####################################################################################

# 5. 캐릭터 만들기
character = pygame.Rect( charobj.get_rect())
character.left = width // 2 - character.width #화면 최대 넓이 / 2 - 캐릭터 크기
character.top = height - character.height # 화면 최대 높이 - 캐릭터 크기
chardx = 0
chardy = 0


# 6.게임 시작 루프
while True:
    display.fill( (255,255,255) ) #화면 배경색 설정
    display.blit(background, (0, 0))

    #캐릭터 조작
    event = pygame.event.poll() # 이벤트 가져오기
    if event.type == pygame.QUIT : #이벤트 타입이 QUIT이면
        break #반복 종료
    elif event.type == pygame.KEYDOWN and gameover == 0 :#키 입력, 게임오버 0
        if event.key == pygame.K_LEFT : #왼쪽 화살표 입력
            chardx = -5
        elif event.key == pygame.K_RIGHT : #오른쪽 화살표 입력
            chardx = 5
    elif event.type == pygame.KEYUP and gameover == 0 :
        if event.key == pygame.K_LEFT:
            chardx = 0
        elif event.key == pygame.K_RIGHT:
            chardx = 0

#미사일 내리기
    if gameover == 0:
        for(obj, speed) in missile:
            obj.top += speed
            if obj.top > height:
                missile.remove( (obj, speed) )
                obj = pygame.Rect(dodge.get_rect())
                obj.left = random.randint(0,width)
                obj.top = -100
                speed = random.randint(3,9)
                missile.append((obj,speed))
                point += 1

        character.left = character.left + chardx
        if character.left < 0:
            character.left = 0
        elif character.left > width - character.width:
            character.left = width - character.width

        for (obj,speed) in missile :
            if obj.colliderect(character): #colliderect : 충돌 검사
                gameover = 1

# 화면 그리기
    for (obj, speed) in missile: #미사일 리스트 물체 개수만큼 반복
        display.blit(dodge, obj) #화면에 물체 그리기

    display.blit(charobj, character) #화면에 캐릭터 그리기

    if gameover == 1:
        font1 = pygame.font.SysFont("malgungothic", 72)
        message = font1.render("게임종료",True, (255,0,0))
        display.blit(message, (200, 350))

    font2 = pygame.font.SysFont("malgungothic", 20)
    scmsg = font2.render ( str(point) , True, (255,255,0))
    display.blit(scmsg,(10,10))



    pygame.display.update() #모든 화면 그리기 업데이트
    time.tick(30) #초당 프레임 수


