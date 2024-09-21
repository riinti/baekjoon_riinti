import sys

input = sys.stdin.readline

n, k = map(int, input().split())
room = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
count = 0

for _ in range(n):
    s, y = map(int, input().split())
    room[y-1][s] += 1

for i in room :
    for j in i:
        if j % k == 0:
            count += j//k
        else:
            count += (j//k) + 1
print(count)