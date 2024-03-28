def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    if n == 1:
        for i in num_list[:b+1]:
        	answer.append(i)
    elif n == 2:
        for i in num_list[a:]:
        	answer.append(i)
    elif n == 3:
        for i in num_list[a:b+1]:
        	answer.append(i)
    elif n == 4:
        for i in range(a, b+1, c):
        	answer.append(num_list[i])
    return answer