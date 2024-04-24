def solution(babbling):
    answer = 0
    tmp = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in tmp:
            if j*2 not in i:
                i = i.replace(j,' ')
        if i.isspace():
            answer += 1
    return answer