import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum = [0]
tmp = 0

for i in numbers:
    tmp = tmp + i
    sum.append(tmp)

# 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])