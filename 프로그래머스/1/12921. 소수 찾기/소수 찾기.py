def solution(n):
    answer = 0
    for i in range(2,n+1):
        isPrime = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0 and i!=j:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer