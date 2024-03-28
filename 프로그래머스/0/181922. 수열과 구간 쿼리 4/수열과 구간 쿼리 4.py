def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    answer = arr
    return answer