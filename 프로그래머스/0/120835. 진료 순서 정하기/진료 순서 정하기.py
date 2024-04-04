def solution(emergency):
    answer = [0]*len(emergency)
    tmp = emergency.copy()
    tmp.sort(reverse=True)
    for i in emergency:
        answer[emergency.index(i)] = tmp.index(i) + 1
    return answer