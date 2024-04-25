def solution(n, lost, reserve):
    reserve_ = set(reserve) - set(lost)
    lost_ = set(lost) - set(reserve)
    for l in lost_:
        if l-1 in reserve_:
            reserve_.remove(l-1)
        elif l+1 in reserve_:
            reserve_.remove(l+1)
        else:
            n -= 1
    return n