def solution(a, b):
    answer = 0
    a, b = str(a), str(b)
    if a + b > b + a:
        answer = a + b
    else:
        answer = b + a
    return int(answer)