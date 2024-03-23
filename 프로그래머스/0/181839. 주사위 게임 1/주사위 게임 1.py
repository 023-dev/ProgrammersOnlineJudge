def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:
        answer = pow(a, 2) + pow(b, 2)
    elif (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer