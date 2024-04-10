def solution(lines):
    answer = 0
    tmp = []
    for line in lines:
        for i in range(line[0], line[1]):
            tmp.append(i)
    for i in set(tmp):
        if tmp.count(i) > 1:
            answer += 1
    return answer