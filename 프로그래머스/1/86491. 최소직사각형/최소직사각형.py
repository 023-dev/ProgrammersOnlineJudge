def solution(sizes):
    answer = 0
    y_max, x_max = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        y_max = max(y_max, sizes[i][0])
        x_max = max(x_max, sizes[i][1])
    answer = x_max * y_max
    return answer