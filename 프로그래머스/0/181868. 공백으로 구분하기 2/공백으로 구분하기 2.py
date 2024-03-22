def solution(my_string):
    answer = []
    str = ''
    for i in my_string:
        if i.isalpha():
            str+=i
        elif len(str) > 0 and not(i.isalpha()):
            answer.append(str)
            str = ''
    if str != '':
        answer.append(str)
    return answer