import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())
count = 1
e = 1
s = 1
m = 1

while True:
    if e == E and s == S and m == M:
        print(count)
        break
    e += 1
    s += 1
    m += 1
    if e>15:
        e = 1
    if s>28:
        s = 1
    if m>19:
        m = 1
    count += 1