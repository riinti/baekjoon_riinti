T = int(input())

for _ in range(T):
    ps = list(input())
    sum = 0

    for j in range(len(ps)):
        if ps[j] == "(":
            sum += 1
        else:
            sum -= 1

        if sum < 0:
            print("NO")
            break

    if sum > 0: 
        print("NO")
    elif sum == 0:  
        print("YES")