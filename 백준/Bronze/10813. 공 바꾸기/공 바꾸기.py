import sys
N, M = map(int, sys.stdin.readline().split())#(1 ≤ N, M ≤ 100)
basket = [i for i in range(1, N+1)]
for m in range(M):
    i, j = map(int, sys.stdin.readline().split()) 
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
for n in range(N):
    print(basket[n], end=' ')