def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        n = 0
        for j in range(1, int((i)**0.5)+1):
            if i % j == 0:
                n += 2
        if i**0.5%1==0:
            n -= 1
        if n > limit:
            answer += power
        else:
            answer += n
        n = 1
    return answer