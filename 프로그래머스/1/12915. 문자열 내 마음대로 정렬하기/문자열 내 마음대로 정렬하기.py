def solution(strings, n):
    answer = []
    strings.sort(key=lambda string : (string[n], string))
    return strings