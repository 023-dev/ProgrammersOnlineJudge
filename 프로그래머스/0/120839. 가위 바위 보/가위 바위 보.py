def solution(rsp):
    answer = ''
    dic = {'0' : '5',
          '2' : '0',
          '5' : '2'}
    for i in rsp:
        answer += dic[i]
    return answer