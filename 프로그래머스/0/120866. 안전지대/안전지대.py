def solution(board):
    answer = 0
    tmp = [[0 for _ in range(len(board))]for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                if j > 0:
                    for k in range(j-1, j+2):
                        try:
                            if i > 0:
                                tmp[i-1][k] = 1
                            tmp[i][k] = 1
                            tmp[i+1][k] = 1
                        except IndexError:
                            pass
                else:
                    for k in range(j, j+2):
                        try:
                            if i > 0:
                                tmp[i-1][k] = 1
                            tmp[i][k] = 1
                            tmp[i+1][k] = 1
                        except IndexError:
                            pass
    for p in range(len(tmp)):
        for q in range(len(tmp[p])):
            if tmp[p][q] == 0:
                answer += 1
    return answer