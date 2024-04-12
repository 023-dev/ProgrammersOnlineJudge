def solution(arr):
    if not(arr):
        return [-1]
    arr.remove(min(arr))
    return arr