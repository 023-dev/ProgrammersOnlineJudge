def solution(lottos, win_nums):
    cnt = 0
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            zeros += 1
    return [rank[cnt+zeros], rank[cnt]]