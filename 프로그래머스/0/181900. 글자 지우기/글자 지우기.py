def solution(my_string, indices):
    answer = ''
    for i in indices:
        my_string = my_string[0:i] + " " + my_string[i+1:]
    answer = my_string.replace(' ', '')
    return answer