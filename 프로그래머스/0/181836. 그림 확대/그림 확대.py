def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        pixel = ''
        for j in range(len(picture[i])):
            pixel += picture[i][j]*k
        for _ in range(k):
            answer.append(pixel)
    return answer