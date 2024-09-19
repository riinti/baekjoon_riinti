import sys

input = sys.stdin.readline

hap = []
for _ in range(7):
    num = int(input())
    if (num % 2) == 1:
        hap.append(num)

if len(hap) != 0:
    print(sum(hap))
    print(min(hap))
else:
    print(-1)