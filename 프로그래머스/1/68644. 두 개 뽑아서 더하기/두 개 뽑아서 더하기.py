def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            try: 
                if answer.index(numbers[i]+numbers[j]):
                    pass
            except ValueError: 
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer