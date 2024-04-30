def solution(s):
    tmp = []
    for c in s:
        if len(tmp) and tmp[-1] == c:
            tmp.pop(-1)
        else:
            tmp.append(c)
    return 0 if len(tmp) else 1