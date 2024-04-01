def solution(my_string, s, e):
    answer = ''
    acc = my_string[s:e+1]
    acc = acc[::-1]
    answer = my_string[:s] + acc + my_string[e+1:]
    return answer