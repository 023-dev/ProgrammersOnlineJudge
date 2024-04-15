def solution(k, score):
    answer = []
    tmp = []
    for i in range(len(score)):
        if len(tmp) >= k:
            tmp.append(score[i])
            tmp.sort()
            answer.append(tmp[-k])
        else:
            tmp.append(score[i])
            tmp.sort()
            answer.append(tmp[0])
    return answer