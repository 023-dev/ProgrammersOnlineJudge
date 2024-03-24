def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        val = numLog[i] - numLog[i-1]
        if val  == 1:
            answer += 'w'
        elif val  == -1:
            answer += 's'
        elif val  == 10:
            answer += 'd'
        elif val  == -10:
            answer += 'a'
    return answer