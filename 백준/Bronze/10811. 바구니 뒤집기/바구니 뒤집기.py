import sys
N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1, N+1)]
for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    slc = basket[i-1:j]
    slc.reverse()
    basket[i-1:j] = slc
for n in range(N):
    print(basket[n], end=' ')