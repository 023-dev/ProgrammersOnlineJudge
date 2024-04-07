def solution(array, height):
    answer = 0
    array.append(height)
    array.sort(reverse=True)
    answer = array.index(height)
    return answer