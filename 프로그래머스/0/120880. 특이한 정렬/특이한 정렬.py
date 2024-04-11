def solution(numlist, n):
    answer = []
    tmp = list(map(lambda x: abs(x - n), numlist))
    s, b = 0, 0
    for i in range(len(tmp)):
        answer.append(numlist[tmp.index(min(tmp))])
        if abs(n-answer[i-1]) == abs(n-answer[i]):
            if answer[i-1] < answer[i]:
                s = answer[i-1]
                b = answer[i]
                answer[i-1] = b 
                answer[i] = s
        tmp[tmp.index(min(tmp))] = 10001
    return answer