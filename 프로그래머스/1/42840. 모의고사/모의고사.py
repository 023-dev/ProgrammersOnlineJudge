def solution(answers):
    answer=[]
    tmp = [0, 0, 0]
    t1 = [1, 2, 3, 4, 5] * len(answers)
    t2 = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    t3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    for i in range(len(answers)):
        tmp[0] += answers[i] == t1[i]
        tmp[1] += answers[i] == t2[i]
        tmp[2] += answers[i] == t3[i]
    for i in range(len(tmp)):
        if max(tmp) == tmp[i]:
            answer.append(i+1)
    return answer