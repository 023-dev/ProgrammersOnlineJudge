def solution(n):
    answer = ''
    acc = list(map(int, str(n)))
    acc.sort(reverse = True)
    for i in acc:
        answer += str(i)
    return int(answer)