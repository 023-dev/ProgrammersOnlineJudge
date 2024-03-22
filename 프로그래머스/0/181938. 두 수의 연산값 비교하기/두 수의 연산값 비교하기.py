def solution(a, b):
    answer = 0
    if (2*a*b) > int(str(a) + str(b)):
        answer = 2*a*b
    elif (2*a*b) < int(str(a) + str(b)):
        answer = int(str(a) + str(b))
    else:
        answer = int(str(a) + str(b))
    return answer