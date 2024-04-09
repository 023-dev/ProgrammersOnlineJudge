def solution(spell, dic):
    answer = 0
    for i in dic:
        for j in spell:
            if j not in i:
                break
            if j == spell[-1]:
                return 1
    return 2