def solution(numbers):
    answer = 0
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    answer = a* b
    return answer