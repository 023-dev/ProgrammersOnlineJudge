def solution(rank, attendance):
    #n명, 3명만, 참여했던 => rank … attendance => a, b, c => 10000*a + 100*b + c => answer … return
    answer = 0
    acc = []
    for i in range(len(attendance)):
        if attendance[i]:
            acc.append(rank[i])
    acc.sort()
    answer = 10000*rank.index(acc[0]) + 100*rank.index(acc[1]) + rank.index(acc[2])
    return answer