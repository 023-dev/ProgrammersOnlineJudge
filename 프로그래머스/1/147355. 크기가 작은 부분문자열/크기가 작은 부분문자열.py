def solution(t, p):
    answer = 0
    for i in range(len(t)+(len(p)*-1)+1):
        if p >= t[i:i+len(p)]:
            answer += 1
    return answer