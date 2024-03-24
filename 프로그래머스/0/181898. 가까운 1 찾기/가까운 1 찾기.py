def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1,idx)
    except ValueError:
        answer = -1
    return answer