import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for _ in range(n):
    site, password = [s.rstrip() for s in (input().split())]
    dict[site] = password

for _ in range(m):
    quest = input().rstrip()
    print(dict[quest])