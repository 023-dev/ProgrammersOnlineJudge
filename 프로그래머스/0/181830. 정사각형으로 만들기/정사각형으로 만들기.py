def solution(arr):
    answer = [[]]
    cols = len(arr[0])
    rows = len(arr)
    if cols > rows:
        for _ in range(cols-rows):
            arr.append([0]*cols)
    elif cols < rows:
        for i in range(len(arr)):
            for _ in range(rows-cols):
                arr[i].append(0)
    answer = arr.copy()
    return answer