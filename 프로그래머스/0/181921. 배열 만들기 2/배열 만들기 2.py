import re
def solution(l, r):
    answer = []
    acc = ''
    for i in range(l, r+1):
        acc = str(i)
        acc = acc.replace('5','')
        acc = acc.replace('0', '')
        if not acc:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer