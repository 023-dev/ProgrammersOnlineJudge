import math
def solution(n):
    answer = 1
    while True:
        fac = math.factorial(answer)
        if fac >= n:
            if fac > n:
                if fac - n > math.factorial(answer-1) - n:
                    answer -= 1
            break
        else:
            answer += 1
    return answer