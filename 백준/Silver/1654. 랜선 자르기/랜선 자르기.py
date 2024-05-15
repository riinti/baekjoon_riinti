import sys

input = sys.stdin.readline

k, n = map(int, input().split())
nlist = [int(input()) for _ in range(k)]
    
start = 1
end = max(nlist)

while (start <= end): #이분탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    mid = (start + end) // 2 #중앙값 정의
    count = 0 
    for i in range(k):
        count += nlist[i] // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)