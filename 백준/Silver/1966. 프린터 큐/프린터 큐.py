import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))

    result = 1
    while len(nlist)>0:
        if nlist[0] >= max(nlist):
            if m == 0: 
                break
            nlist.pop(0)
            result += 1
        else:
            nlist.append(nlist.pop(0))

        if m > 0:
            m = m - 1 
        else:
            m = len(nlist) - 1

    print(result)