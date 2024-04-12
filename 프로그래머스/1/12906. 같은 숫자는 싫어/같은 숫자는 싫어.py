def solution(arr):    
    answer = [arr[0]]
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer += [arr[i]]
    return answer