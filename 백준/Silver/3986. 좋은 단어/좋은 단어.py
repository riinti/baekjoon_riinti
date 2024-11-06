import sys

input = sys.stdin.readline

n = int(input().rstrip())
ans = 0

for _ in range(n):
    stack = []
    nlist = list(input().rstrip())
    
    for i in nlist:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not len(stack):
        ans += 1 

print(ans)