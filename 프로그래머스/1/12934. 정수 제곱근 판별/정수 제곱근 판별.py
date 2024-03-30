import math
def solution(n):
    answer = 0
    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        answer = pow(math.sqrt(n)+1, 2)
    else:
        answer = -1
    return answer