def solution(babbling):
    answer = 0
    tmp = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in tmp:
            if j in i:
                i = i.replace(j, ' ')
                if not(i.strip()):
                    answer += 1
                    break
    return answer