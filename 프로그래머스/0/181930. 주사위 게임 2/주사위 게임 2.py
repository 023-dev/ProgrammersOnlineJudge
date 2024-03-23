def solution(a, b, c):
    answer = 0
    if a != b and a != c and b != c:
        answer = a+b+c
    elif (a == b and a != c) or (c == b and a != c) or (a == c and b != c):
        answer = (a+b+c) * (pow(a, 2)+pow(b, 2)+pow(c, 2))
    elif a == b and a == c:
        answer = (a+b+c) * (pow(a, 2)+pow(b, 2)+pow(c, 2)) * (pow(a, 3)+pow(b, 3)+pow(c, 3))
    return answer