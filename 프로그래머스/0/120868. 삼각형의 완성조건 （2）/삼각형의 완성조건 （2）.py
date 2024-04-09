def solution(sides):
    answer = 0
    s, b = sides[0], sides[1]
    if s > b:
        s, b = b, s
    for i in range(b-s+1, b+1):
        answer += 1
    if answer != 1:
        for i in range(b+1, s+b):
                answer += 1
    return answer