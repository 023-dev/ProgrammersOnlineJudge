def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        answer.append(-1)
        for i in range(s, e+1):
            if arr[i] > k :
                if answer[-1] == -1:
                    answer[-1] = arr[i]
                elif answer[-1] != -1 and arr[i] < answer[-1]:
                    answer[-1] = arr[i]
    return answer