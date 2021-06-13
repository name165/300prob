def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 4: #타일 길이를 6으로 나눈 나머지가 1이나 2일시 r을 3번 써야되므로 안되고 4일 시에는 b를 2번 써야하므로 불가능
        answer = '-1'
    else:
        for i in range(tile_length): # 타일 길이 만큼 반복
            answer += com[i % 6] #answer에 com 추가
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
tile_length1 = 11
ret1 = solution(tile_length1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")