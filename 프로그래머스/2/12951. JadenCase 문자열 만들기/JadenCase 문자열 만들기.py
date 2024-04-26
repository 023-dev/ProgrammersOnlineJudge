def solution(s):
    answer = ''
    for i in range(len(s)): 
        if s[i] == ' ':
            answer += s[i]
        else:
            if len(answer)==0 or answer[-1]==' ':
                answer += s[i].upper()
            else:
                answer += s[i].lower()
    return answer