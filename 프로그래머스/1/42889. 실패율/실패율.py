def solution(N, stages):
    answer = []
    tmp = [0 for _ in range(N+1)]
    for i in range(len(tmp)):
        tmp[i] = stages.count(i+1)
    for i in range(N):
        try:
            answer.append(tmp[i]/sum(tmp[i:]))
        except ZeroDivisionError:
            answer.append(0)
    answer = sorted(range(len(answer)), key=lambda i: answer[i],reverse=True)
    return list(map(lambda x:x +1, answer))