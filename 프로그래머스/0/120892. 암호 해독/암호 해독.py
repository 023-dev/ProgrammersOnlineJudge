def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        print(i)
        answer += cipher[i]
    return answer