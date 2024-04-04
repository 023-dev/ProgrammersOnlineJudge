import math
def solution(balls, share):
    answer = 0
    numer = math.factorial(balls)
    denom = math.factorial(balls - share) * math.factorial(share)
    answer = numer / denom
    return answer