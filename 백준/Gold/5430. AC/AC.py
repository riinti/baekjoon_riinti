import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().strip("[]\n").split(","))

    temp = False
    r_count = 0

    if n == 0:
        arr = deque()

    for i in p:
        if i == 'R':
            r_count += 1
        elif i == 'D':
            if len(arr)!=0:
                if r_count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                temp = True
                break
    if not temp:
        if r_count % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")