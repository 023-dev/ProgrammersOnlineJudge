def solution(keyinput, board):
    answer = [0,0]
    x_max = (board[0]-1)//2
    y_max = (board[1]-1)//2
    for i in keyinput:
        if i == "up":
            answer[1] += 1
        elif i == "down":
            answer[1] -= 1
        elif i == "left":
            answer[0] -= 1
        elif i == "right":  
            answer[0] += 1
        if abs(answer[0]) > x_max:
            if answer[0] > x_max:
                answer[0] = x_max
            else:
                answer[0] = x_max * -1 
        if abs(answer[1]) > y_max:
            if answer[1] > y_max:
                answer[1] = y_max
            else:
                answer[1] = y_max * -1
    return answer