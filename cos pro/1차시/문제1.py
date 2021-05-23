#문제 1 : 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기

def solution(shirt_size) :
    answer = [ ]
    answer = [0, 0, 0, 0, 0, 0]
    for i in shirt_size: # 리스트 반복 => 리스트 내 항목을 변수에 하나씩 대입
        if i == "XS": answer[0] += 1
        elif i == "S": answer[1] += 1
        elif i == "M": answer[2] += 1
        elif i == "L": answer[3] += 1
        elif i == "XL": answer[4] += 1
        elif i == "XXL": answer[5] += 1
    return answer

shirt_size = ["XS","S","L","L","XL","S"]
ret = solution(shirt_size)

print("solution : return value of the fuction is ", ret)

