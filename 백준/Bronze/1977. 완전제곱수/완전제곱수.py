m = int(input())
n = int(input())
nlist = []
for i in range(m, n+1):
    T = int(i ** 0.5) ** 2
    if i == T:
        nlist.append(i)

if len(nlist)>0:
    print(sum(nlist))
    print(min(nlist))
else:
    print(-1)