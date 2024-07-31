import sys

input = sys.stdin.readline

n = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+(nlist[-1][0])+1) #dp의 각 항목은 그 일자까지의 최대 비용

for i in range(n):
    end_day = i+nlist[i][0]
    for j in range(end_day,n+1):
        if dp[j]<dp[i]+nlist[i][1]:
            dp[j] = dp[i]+nlist[i][1]
print(dp[n])