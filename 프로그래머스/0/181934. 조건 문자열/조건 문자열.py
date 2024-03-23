def solution(ineq, eq, n, m):
    answer = 0
    if m == n and eq == '=':
        answer = 1
    else:
        if n < m:
            if ineq == "<":
                answer = 1
        else:
            if ineq == ">":
                answer = 1
                
    return answer