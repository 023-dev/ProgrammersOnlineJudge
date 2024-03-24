def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        j, k = queries[i]
        arr[j], arr[k] = arr[k], arr[j]
    answer = arr
    return answer