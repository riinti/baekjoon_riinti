import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))

time = [0 for i in range(257)] # time[k]에 땅높이가 k일때의 소요시간 저장
height = 0

for lv in range(257):
    block = b # 인벤토리에 남은 블록 수
    for i in ground:
        if i <= lv: # i == g이면 g-i=0
            time[lv] += lv - i
            block -= lv - i
        else:
            time[lv] += 2 * (i - lv)
            block += i - lv
    if block >= 0 and time[lv] <= time[height]: # 땅의 높이가 가장 높은 것을 저장
        height = lv

print(time[height], height)