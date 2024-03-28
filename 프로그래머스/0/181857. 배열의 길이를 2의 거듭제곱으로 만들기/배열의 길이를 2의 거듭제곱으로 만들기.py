import math
def solution(arr):
    answer = arr
    n = len(arr)
    if math.log2(n) > math.floor(math.log2(n)):
        for _ in range(pow(2, math.ceil(math.log2(n)))-n):
            answer.append(0)
    return answer