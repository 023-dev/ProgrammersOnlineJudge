import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = 0
    denom = 0
    if denom2 < denom1:
        denom1, denom2, numer1, numer2 = denom2, denom1, numer2, numer1
    if denom2 % denom1 == 0:
        numer1 *= denom2/denom1
        numer = numer1+numer2
        denom = denom2
    else:
        denom = denom2*denom1
        numer = numer1*(denom/denom1) + numer2*(denom/denom2)
    if math.gcd(int(denom), int(numer)) > 1:
        gcd = math.gcd(int(denom), int(numer))
        denom /= gcd
        numer /= gcd
    answer.append(numer)
    answer.append(denom)    
    return answer