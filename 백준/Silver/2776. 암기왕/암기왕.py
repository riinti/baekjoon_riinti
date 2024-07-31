import sys

input = sys.stdin.readline

def binary_search(start, end, note1, num):
    while start <= end:
        mid = (start+end)//2
        if note1[mid] == num:
            return 1
        elif note1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for _ in range(int(input())):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    for num in note2:
        print(binary_search(0, n-1, note1, num))