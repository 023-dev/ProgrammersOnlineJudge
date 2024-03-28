def solution(order):
    answer = 0
    #americano = 4500, latte = 5000
    #anything => americano => 4500
    #in order list
    for i in order:
        if 'cafelatte' in i:
            answer += 5000
        else:#americano, anything
            answer += 4500
    return answer