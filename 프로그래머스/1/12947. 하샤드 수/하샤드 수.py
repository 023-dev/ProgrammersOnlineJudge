def solution(x):
    answer = False
    acc = 0
    for i in str(x):
        acc += int(i)
    if x % acc == 0:
        answer = True
    return answer