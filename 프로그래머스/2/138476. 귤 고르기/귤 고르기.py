from collections import Counter
def solution(k, tangerine):
    answer = 0
    tmp = sorted(Counter(tangerine).items(), reverse=True, key=lambda key:key[1])
    for key, val in tmp:
        if k <= 0:
            break
        k -= val
        answer += 1
    return answer