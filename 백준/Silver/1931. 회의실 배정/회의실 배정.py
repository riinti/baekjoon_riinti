import sys

input = sys.stdin.readline

n = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(n)]
nlist = sorted(nlist, key=lambda x:(x[1], x[0]))  #x[1]값으로 정렬하고 x[1]값이 같은 애들만 다시 x[0]으로 정렬

count = 0
end_time = 0

for s, e in nlist:
    if s >= end_time:
        end_time = e
        count += 1

print(count)
