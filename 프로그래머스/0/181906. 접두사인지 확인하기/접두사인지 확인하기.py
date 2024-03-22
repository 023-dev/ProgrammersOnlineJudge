def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)):
        if is_prefix == my_string[:i]:
            answer = 1
    return answer