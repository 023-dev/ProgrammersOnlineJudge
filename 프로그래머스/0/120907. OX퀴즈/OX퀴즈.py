def solution(quiz):
    answer = []
    idx = 0
    for i in quiz:
        idx = i.find(' = ')
        if eval(i[:idx]) == int(i[idx+3:]):
            answer.append('O')
        else:
            answer.append('X')
    return answer