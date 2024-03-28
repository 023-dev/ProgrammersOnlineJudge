def solution(q, r, code):
    #q, r, code => code's index % q == r => code[index]
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer