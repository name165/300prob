#문제81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)
#문제82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)
#문제83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b  = scores
print(valid_score)
#문제84
temp = {}
#문제85
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)
#문제86
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)
#문제87
print("메로나 가격:", ice["메로나"])
print(ice)
#문제88
ice["메로나"] = 1300
print(ice)
#문제89
del(ice["메로나"])
print(ice)
#90
#누가바라는 key값에 대응되는 value값이 없음
