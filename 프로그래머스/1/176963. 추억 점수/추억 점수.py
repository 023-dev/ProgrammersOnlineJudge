def solution(name, yearning, photo):
    answer = []
    tmp = 0
    for i in photo:
        for j in i:
            if j in name:
                tmp += yearning[name.index(j)]
        answer.append(tmp)
        tmp = 0
    return answer