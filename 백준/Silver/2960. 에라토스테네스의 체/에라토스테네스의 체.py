import sys

input = sys.stdin.readline
                
n,k = map(int, input().split())
count = 0
array =[True for i in range(n+1)]
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if array[j]:
            array[j] = False
            count += 1
            if count == k:
                print(j)