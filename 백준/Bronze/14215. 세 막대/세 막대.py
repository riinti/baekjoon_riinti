nlist = sorted(list(map(int, input().split())))
if nlist[0] + nlist[1] > nlist[2]:
    print(sum(nlist))
else:
    print((nlist[0] + nlist[1]) * 2 - 1)