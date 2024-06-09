import sys

input = sys.stdin.readline

people = int(input())
plist = list(map(int, input().split()))
plist.sort()
time = 0

for i in range(people):
    for j in range(0, i+1):
      time += plist[j]

print(time)