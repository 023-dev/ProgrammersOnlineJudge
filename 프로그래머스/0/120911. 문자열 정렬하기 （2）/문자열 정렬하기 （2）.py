def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = sorted(my_string)
    answer = ''.join(my_string)
    return answer