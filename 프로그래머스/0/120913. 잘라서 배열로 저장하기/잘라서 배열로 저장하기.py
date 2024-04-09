def solution(my_str, n):
    answer = []
    tmp = ''
    for i in range(len(my_str)):
        if i % n == 0 and i != 0:
            answer.append(tmp)
            tmp = ''
        tmp += my_str[i]
    if len(tmp) > 0:
        answer.append(tmp)
    return answer