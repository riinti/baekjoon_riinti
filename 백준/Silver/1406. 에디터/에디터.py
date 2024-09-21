import sys

input = sys.stdin.readline

llist = list(input().rstrip())
rlist = []
t = int(input())

for _ in range(t):
    data = list(input().split())
    if data[0] == 'B':
        if llist: 
            llist.pop()
    elif data[0] == 'L': 
        if llist:
            rlist.append(llist.pop())
    elif data[0] == 'D': 
        if rlist:
            llist.append(rlist.pop())
    elif data[0] == 'P':
        llist.append(data[1])

ans = llist + rlist[::-1]
print(''.join(ans))