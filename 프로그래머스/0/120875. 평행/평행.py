def solution(dots):
    answer = 0
    dots.sort()
    if abs(dots[0][1] - dots[1][1]) / abs(dots[0][0] - dots[1][0]) == abs(dots[2][1] - dots[3][1]) / abs(dots[2][0] - dots[3][0]) or abs(dots[1][1] - dots[3][1]) / abs(dots[1][0] - dots[3][0]) == abs(dots[0][1] - dots[2][1]) / abs(dots[0][0] - dots[2][0]):
        return 1
    return answer