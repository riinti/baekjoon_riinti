nlist = list(map(int, input().split()))
mlist = list(map(int, input().split()))

n = sum(nlist)
m = sum(mlist)
if n>m:
    print(n)
elif n<m:
    print(m)
else:
    print(n)