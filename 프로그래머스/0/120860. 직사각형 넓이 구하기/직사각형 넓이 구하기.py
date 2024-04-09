def solution(dots):
    dots.sort()
    v = abs(dots[0][1] - dots[1][1])
    h = abs(dots[0][0] - dots[2][0])
    return v*h