def solution(num_list):
    answer = 0
    acc = 1
    for i in num_list:
        acc = acc * i
    print(pow(sum(num_list), 2))
    if acc < pow(sum(num_list), 2):
        answer = 1
    return answer