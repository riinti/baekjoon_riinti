a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sum = 0
b_sum = 0
cnt = 0

for i in range(9):
    a_sum += a[i]
    if a_sum > b_sum and cnt == 0:
        cnt += 1
    if a_sum < b_sum and cnt == 1:
        cnt += 1
    b_sum += b[i]

if cnt == 2 and a_sum < b_sum:
    print("Yes")
elif cnt == 1 and a_sum < b_sum:
    print("Yes")
else:
    print("No")