#문제51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
#문제52
movie_rank.append("배트맨")
print(movie_rank)
#문제53
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
#문제54
movie_rank.remove("럭키")
print(movie_rank)
#문제55
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)
#문제56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
#문제57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max :", max(nums))
print("min :", min(nums))
#문제58
nums = [1, 2, 3, 4 ,5]
print(sum(nums))
#문제59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
#문제60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))