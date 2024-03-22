def solution(arr, n):
    answer = arr
    if len(arr) % 2 != 0:
        for i in range(0, len(arr)):
            if i % 2 == 0:
                answer[i] += n
    else:
        for i in range(0, len(arr)):
            if i % 2 != 0:
                answer[i] += +n
    print(answer)
    return answer