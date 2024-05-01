def solution(arr):
    tmp = 1
    for a in arr:
        tmp *= a
    for t in range(max(arr), tmp+1):
        flag = True
        for a in arr:
            if t % a != 0:
                flag = False
                break
        if flag:
            return t