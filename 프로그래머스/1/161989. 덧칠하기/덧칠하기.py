def solution(n, m, section):
    answer = 0
    j = 0
    tmp = [1 for _ in range(n)]
    for i in section:
        tmp[i-1] = 0
    while j < len(tmp):
        if tmp[j]==0:
            tmp[j:j+m] = [1]*m
            j+=m
            answer+=1
        else:
            j+=1
    return answer