def solution(myString):
    answer = []
    answer = myString.split('x')
    answer = list(filter(None, answer))
    answer.sort()
    return answer