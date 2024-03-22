def solution(my_string, overwrite_string, s):
    answer = ''
    my_string = list(my_string)
    for i in range(len(my_string)):
        if i >= s and i < s+len(overwrite_string):
            answer += overwrite_string[i-s]
        else:
            answer += my_string[i]
        print(i)
    print(answer)
    return answer