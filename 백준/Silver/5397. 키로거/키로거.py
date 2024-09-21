import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    llist = []
    rlist = []
    data = input().rstrip()
    for i in data:
        if i == '-':
            if llist: 
                llist.pop()
        elif i == '<': 
            if llist:
                rlist.append(llist.pop())
        elif i == '>': 
            if rlist:
                llist.append(rlist.pop())
        else:
            llist.append(i)
    llist.extend(reversed(rlist))
    print(*llist,sep="")