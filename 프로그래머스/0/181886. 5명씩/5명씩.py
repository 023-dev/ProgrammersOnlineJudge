def solution(names):
    answer = []
    '''
    최소 5명, 사람들 리스트, 5명씩 그룹의 가장 앞에 사람을 리턴
    '''
    for i in range(0, len(names), 5):
        answer.append(names[i])
    return answer