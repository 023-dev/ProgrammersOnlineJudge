def solution(num, total):
    answer = []
    for i in range(total//num-num,total//num+num):
        answer.append(i)
        if len(answer) == num:
            if sum(answer) == total:
                return answer
            else:
                answer.pop(0)