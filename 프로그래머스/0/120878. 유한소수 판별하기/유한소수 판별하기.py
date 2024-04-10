import math
def solution(a, b):
    if a % b == 0:
        return 1
    tmp = math.gcd(a,b)
    tmp = b // tmp
    for i in range(2, tmp+1):
        if tmp%i==0:
            if i%2 == 0 or i % 5 == 0:pass
            else:return 2
    return 1