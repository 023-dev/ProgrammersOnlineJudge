def solution(strArr):
    tmp = [0]*len(strArr)
    for i in strArr:
        tmp[len(i)] += 1
    return max(tmp)