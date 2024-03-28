def solution(my_string):
    answer = [0]*26*2
    my_string = sorted(my_string)
    ln, dn = ord('A'), ord('a')
    hrf = int(len(answer)/2)
    for i in range(len(answer)):
        if i < hrf:
            if chr(ln+i) in my_string:
                answer[i] += my_string.count(chr(ln+i))
        else:
            if chr(dn+i-hrf) in my_string:
                answer[i] += my_string.count(chr(dn+i-hrf))
    return answer