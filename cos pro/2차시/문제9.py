def solution(votes, N, K):
    counter = [0 for _ in range(N+1)]
    for x in votes :
        counter[x] += 1
    answer = 0 #-1 -> 0
    for c in counter:
        if c == K:
            answer += 1
    return answer

votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
print(solution(votes, N, K))