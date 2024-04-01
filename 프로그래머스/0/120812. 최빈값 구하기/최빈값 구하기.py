def solution(array):
    answer = sorted(set(array), key = array.count)
    if len(answer) > 1:
        if array.count(answer[-2]) == array.count(answer[-1]):
            return -1
    return answer[-1]