def solution(myString):
    answer = ''
    for i in myString.lower():
        if i == 'a':
            answer += i.upper()
        else:
            answer += i
    return answer