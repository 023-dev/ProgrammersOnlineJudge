def solution(my_string, queries):
    answer = ''
    reverse = ''
    for i in queries:
        s, e = i
        reverse = my_string[s:e+1]
        my_string = my_string[:s] + reverse[::-1] + my_string[e+1:]
    answer = my_string
    return answer