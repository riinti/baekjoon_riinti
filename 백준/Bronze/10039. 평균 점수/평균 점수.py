import sys

input = sys.stdin.readline
score = []
for _ in range(5):
    score.append(int(input()))

total = 0
avg = 0

for i in range(len(score)):
    score[i] = int(score[i])
    if score[i] < 40 :
        score[i] = 40

    total = score[i] + total

avg = total // 5
print(avg)