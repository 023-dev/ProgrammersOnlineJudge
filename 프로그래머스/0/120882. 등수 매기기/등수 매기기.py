def solution(score):
    answer = []
    tmp = []
    for i in score:
        tmp.append(sum(i)/len(i))
    answer=tmp.copy()
    tmp.sort(reverse=True)
    for i in range(len(answer)):
        answer[i] = tmp.index(answer[i])+1
    return answer