def solution(A, B):
    if A == B:return 0
    tmp = A
    for i in range(len(A)):
        if tmp[-1] + tmp[:-1] == B:
            return i+1
        else:
            tmp = tmp[-1] + tmp[:-1]
    return -1