import sys
N, M = map(int, sys.stdin.readline().split())#(1 ≤ N, M ≤ 100)
basket = [0 for i in range(N)]
for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i-1, j):
        basket[idx] = k
for n in range(N):
    print(basket[n], end=' ')