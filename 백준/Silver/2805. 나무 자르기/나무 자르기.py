import sys

input = sys.stdin.readline

def biany(array, target, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = ((start+end)//2)
        for i in array:
            if i>mid:
                total += i - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)

N, M = map(int, input().split())
height = list(map(int, input().split()))

biany(height, M, 0, max(height))