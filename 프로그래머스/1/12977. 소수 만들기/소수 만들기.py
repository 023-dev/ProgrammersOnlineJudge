from itertools import combinations
def solution(nums):
    tmp = list(combinations(nums, 3))
    sum = 0
    answer = 0
    for i in range(len(tmp)):
        isPrime = True
        sum = tmp[i][0]+tmp[i][1]+tmp[i][2]
        for j in range(2, sum):
            if sum % j == 0:
                isPrime = False
                break
        if isPrime:
            answer+=1
    return answer