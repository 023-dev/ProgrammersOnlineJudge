def solution(age):
    answer = ''
    tmp = str(age)
    for i in range(len(tmp)):
        answer += chr(int(tmp[i])+97)
    return answer