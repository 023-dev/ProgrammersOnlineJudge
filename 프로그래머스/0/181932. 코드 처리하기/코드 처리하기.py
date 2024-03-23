def solution(code):
    answer = ''
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1":
                if idx % 2 == 0:  
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != '1' :
                if idx % 2 != 0:
                    ret += code[idx]
            else:
                mode = 0
        #print("idx :", idx, " code[idx] :", code[idx], "mode :", mode, 'ret :', ret)
    answer = ret
    if len(answer) == 0:
        answer = 'EMPTY'
    return answer