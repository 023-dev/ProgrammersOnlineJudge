def solution(a, b, n):
    answer = 0
    tmp = 0
    while n >= a:
        answer += n//a * b
        n = n//a * b  + n%a
        print(n)
    return answer