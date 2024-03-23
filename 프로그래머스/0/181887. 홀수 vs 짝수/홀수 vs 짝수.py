def solution(num_list):
    answer = 0
    odd, even = 0, 0
    for i in range(1, len(num_list)+1):
        if i % 2 == 0:
            even += num_list[i-1]
        else:
            odd += num_list[i-1]
    if even < odd:
        answer = odd
    elif even > odd:
        answer = even
    else:
        answer = odd
    return answer