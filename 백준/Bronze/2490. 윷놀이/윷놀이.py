import sys

input = sys.stdin.readline

for _ in range(3):
    nlist = list(map(int, input().split()))
    front = 0
    for i in nlist:
        if i == 0:
            front += 1
    if front == 0:
        print("E")
    elif front == 1:
        print("A")
    elif front == 2:
        print("B")
    elif front == 3:
        print("C")
    elif front == 4:
        print("D")
        