def solution(s):
    idx, zeros = 0, 0
    while s != '1':
        zeros += s.count('0')
        s = s.replace("0",'')
        s = bin(len(s))[2:]
        idx += 1
    return [idx, zeros]