def solution(s):
    tmp = 0
    for c in s:
        if c == "(":
            tmp += 1
        else:
            if tmp > 0:
                tmp -=1
            else:
                return False
    if tmp > 0:
        return False
    else:
        return True