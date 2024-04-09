def solution(s):
    answer = 0
    tmp = s.split()
    for i in range(len(tmp)):
        if tmp[i] == 'Z':
            answer -= int(tmp[i-1])
        else:
            answer += int(tmp[i])
    return answer