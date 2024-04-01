def solution(numbers):
    answer = ''
    dic = {
        "zero" : 0, 
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    number = ''
    for i in numbers:
        number += i
        if number in dic:
            numbers.replace(number, '')
            answer += str(dic[number])
            number = ''
    return int(answer)