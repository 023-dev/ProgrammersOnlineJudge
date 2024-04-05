def solution(array, n):
    answer = 0
    tmp = []
    array.sort()
    for i in array:
        tmp.append(abs(n-i))
    answer = array[tmp.index(min(tmp))]
    return answer