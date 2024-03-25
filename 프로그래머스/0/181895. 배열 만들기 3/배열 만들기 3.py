def solution(arr, intervals):
    answer = []
    for i, j in intervals:
        for k in arr[i:j+1]:
            answer.append(k)
    return answer