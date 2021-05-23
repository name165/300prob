#문제3
def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in (month_list[:month+1]):
        total += i
    total += day
    return total - 1

def solution(start_month,start_day,end_month,end_day):
    start_total = func_a(start_month, start_day) #시작 날짜 
    end_total = func_a(end_month, end_day)
    return end_total - start_total

start_month = 1 #시작 날짜 달
start_day = 2 #시작 날짜 일
end_month = 2 #끝 날짜 달
end_day = 2 #끝 날짜 일
ret = solution(start_month,start_day, end_month,end_day)
print(ret)
