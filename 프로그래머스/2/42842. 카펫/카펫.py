def solution(brown, yellow):
    answer = []
    tot = brown + yellow
    if yellow == 1:
        return [3,3]
    for i in range(3, tot//2+1):
        for j in range(i, tot//i+1):
            if i*j == tot and (i-2)*(j-2)==yellow:
                return [j,i]