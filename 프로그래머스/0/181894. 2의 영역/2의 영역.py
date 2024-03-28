def solution(arr):
    answer = []
    strt, end = 0, 0
    if arr.count(2) > 1:
        arr.reverse()
        end = arr.index(2)
        arr.reverse()
        strt = arr.index(2)    
        answer = arr[strt:-end]
        if end == 0:
            answer = arr
    elif arr.count(2) == 1:
        answer.append(2)
    else:
        answer.append(-1)
    return answer