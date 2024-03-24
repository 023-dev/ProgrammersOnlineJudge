def solution(n):
    answer = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(0)
        arr[i] = 1
        answer.append(arr)
    return answer