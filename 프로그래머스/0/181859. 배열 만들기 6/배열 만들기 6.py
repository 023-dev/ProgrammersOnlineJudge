def solution(arr):
    answer = []
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    answer = stk.copy()        
    if not answer:
        answer.append(-1)
    return answer