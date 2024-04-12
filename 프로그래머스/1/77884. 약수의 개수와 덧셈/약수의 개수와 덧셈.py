def solution(left, right):
    answer = 0
    tmp = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if (i//j) * j == i:
                tmp.append(j)
        print(i, tmp)
        if len(tmp) % 2 == 0:
            answer += i
        else:
            answer -= i
        tmp = []
    return answer