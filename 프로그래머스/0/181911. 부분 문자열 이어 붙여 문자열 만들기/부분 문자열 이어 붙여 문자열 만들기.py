def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        start = parts[i][0]
        end = parts[i][1]+1
        slice = my_strings[i]
        answer += slice[start:end]
    return answer