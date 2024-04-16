def solution(s):
    answer = []
    tmp = ''
    for i in range(len(s)):
        if s[:i].find(s[i]) > -1:
            tmp = s[:i]
            answer.append(tmp[::-1].index(s[i])+1)
            #answer.append(i - s[:i].index(s[i], s[:i].count(s[i])))
            #print(s[:i].index(s[i]), s[:i].count(s[i]))
        else:
            answer.append(s[:i].find(s[i]))
    return answer