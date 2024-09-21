import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(sorted,list(input().split()))
    if a==b:
        print("Possible")
    else:
        print("Impossible")
    