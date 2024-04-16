def solution(n, arr1, arr2):
    answer = []
    tmp = ''
    for i, j in zip(arr1, arr2):
        tmp = bin(i|j)[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    return answer