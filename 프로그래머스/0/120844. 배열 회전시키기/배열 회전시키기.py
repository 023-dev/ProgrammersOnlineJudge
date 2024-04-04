def solution(numbers, direction):
    answer = [0]*len(numbers)
    if direction == 'right':
        for i in range(len(numbers)):
            if i == len(numbers)-1:
                answer[0] = numbers[i]
            else:
                answer[i+1] = numbers[i]
    else:
        for i in range(len(numbers)):
            if i == 0:
                answer[-1] = numbers[i]
            else:
                answer[i-1] = numbers[i]       
    return answer