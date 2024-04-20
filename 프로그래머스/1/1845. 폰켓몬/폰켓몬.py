def solution(nums):
    answer = []
    for i in nums:
        if i not in answer:
            answer.append(i)
    if len(nums)//2 < len(answer):
        return len(nums)//2
    else:
        return len(answer)