def solution(n):
    tmp = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n,3)
        tmp += str(mod)
    tmp.lstrip('0')
    for i in range(len(tmp)):
        answer += int(tmp[i])*3**(len(tmp)-i-1)
    return answer
