import sys

input = sys.stdin.readline

def binary(target, arr):  # 이분 탐색: target보다 작거나 같은 값의 최대 인덱스 반환
    start = 0
    end = len(arr) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n = int(input())
mlist = [tuple(map(int, input().split())) for _ in range(n)]
mlist.sort(key=lambda x: x[1])  # 종료 시간을 기준으로 정렬

dp = [0] * n  # 각 회의까지의 최대 인원
dp[0] = mlist[0][2]

end_time = [mlist[i][1] for i in range(n)] 

for i in range(1, n): #i번째 회의 '이전'에 들어갈 수 있는 인원 수 구하기
    idx = binary(mlist[i][0], end_time)
    if idx != -1:  
        dp[i] = max(dp[i - 1], dp[idx] + mlist[i][2])
    else: 
        dp[i] = max(dp[i - 1], mlist[i][2])

print(dp[n - 1])