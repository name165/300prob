#문제5

def solution(attack, recovery, hp):
    count = 0
    while True:
        count += 1
        hp -= attack
        if hp <= 0:
            return count
        hp += recovery

attack = 30
recovery = 10
hp = 60
ret = solution(attack,recovery,hp)

print(ret)