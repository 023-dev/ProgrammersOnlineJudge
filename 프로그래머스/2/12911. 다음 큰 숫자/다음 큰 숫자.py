def solution(n):
    m = n + 1
    while True:
        if bin(n).count('1') == bin(m).count('1'):
            break
        m +=1
    return m