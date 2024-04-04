def solution(before, after):
    answer = 1
    for i in before:
        if after.count(i) != before.count(i):
            return 0
    return answer