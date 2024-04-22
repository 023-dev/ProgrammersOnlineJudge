def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    i = 1
    if len(score) < m:
        return 0
    while True:
        answer += score[m*i-1] * m
        if len(score)-m*i < m:
            break
        else:
            i += 1
    return answer