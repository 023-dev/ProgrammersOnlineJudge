import math
def solution(num_list, n):
    answer = [[0 for _ in range(n)]for _ in range(math.ceil(len(num_list)/n))]
    y, x = 0, 0
    for i in num_list:
        answer[y][x] = i
        x += 1
        if x == n:
            y += 1
            x = 0
    return answer