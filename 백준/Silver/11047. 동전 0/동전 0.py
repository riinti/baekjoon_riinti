import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
count = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    count += k // i
    k %= i

print(count)
