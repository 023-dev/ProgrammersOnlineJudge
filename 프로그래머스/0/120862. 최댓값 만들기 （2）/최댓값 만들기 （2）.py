def solution(numbers):
    answer = 0
    if max(numbers) == min(numbers):
        return numbers[0] * numbers[1]
    else:
        answer = max(numbers) * min(numbers)
    for i in numbers:
        for j in numbers:
            if i != j:
                if answer < i*j:
                    answer = i*j
    return answer