def solution(my_string):
    answer = []
    tmp = ''
    for i in my_string:
        if i.isdigit():
            tmp += i
        else:
            if len(tmp) > 0:
                answer.append(int(tmp))
            tmp = ''
    if len(tmp) > 0:
        answer.append(int(tmp))
    return sum(answer)