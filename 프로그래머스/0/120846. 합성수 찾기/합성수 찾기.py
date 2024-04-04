def solution(n):
    answer = 0
    tmp = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0: 
                tmp += 1
        if tmp > 2:
            answer += 1
            tmp = 0
        else:
            tmp = 0
    return answer