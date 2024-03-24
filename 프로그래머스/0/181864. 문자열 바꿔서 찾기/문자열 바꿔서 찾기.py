def solution(myString, pat):
    answer = 0
    newString = ''
    for i in range(len(myString)):
        if myString[i] == 'A':
            newString += 'B'
        elif myString[i] == 'B':
            newString += 'A'
    if pat in newString:
        answer = 1
    return answer