import sys

input = sys.stdin.readline

cards = [i for i in range(1,21)]
for _ in range(10):
    a,b = map(int,input().split())
    a-=1
    cards[a:b] = cards[a:b][::-1]
print(*cards)