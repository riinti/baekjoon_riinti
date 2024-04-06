import sys

input = sys.stdin.readline

nlist =[]

for _ in range(9):
  number = int(input())
  nlist.append(number)

print(max(nlist))
print(nlist.index(max(nlist))+1)