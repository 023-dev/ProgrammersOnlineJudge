def solution(dartResult):
    dart = ''
    round = ''
    arr = []
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    for i in range(len(dartResult)):
        dart = dartResult[i]
        if dart.isdigit():
            if i:
                if dartResult[i-1].isdigit():
                    round += dart
                else:
                    arr.append(int(eval(round)))
                    round = dart
            else:
                round = dart
        else:
            if dart in bonus:
                round += '**'+str(bonus.index(dart)+1)
            if dart in option:
                if dart == '*':
                    if len(arr):
                        arr[-1] *= 2
                        round += '*2'
                    else:
                        round += '*2'
                else:
                    round += '*-1'
    arr.append(int(eval(round)))
    return sum(arr)