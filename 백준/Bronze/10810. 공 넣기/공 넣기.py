import sys

input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    x, y, i = map(int, input().split())
    for j in range(x, y+1):
        baskets[j-1] = i

print(*baskets, sep=" ")