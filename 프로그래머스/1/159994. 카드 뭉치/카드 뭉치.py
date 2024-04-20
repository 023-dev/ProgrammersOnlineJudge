def solution(cards1, cards2, goal):
    answer = ''
    tmp = []
    c1, c2 = 0, 0
    for g in goal:
        if len(cards1) > c1 and cards1[c1] == g:
            tmp.append(cards1[c1])
            c1+=1
        elif len(cards2) > c2 and cards2[c2] == g:
            tmp.append(cards2[c2])
            c2+=1
    if tmp == goal:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer