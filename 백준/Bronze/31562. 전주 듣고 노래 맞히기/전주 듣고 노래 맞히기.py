import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic_song = {}
for _ in range(n):
    song = input().split()
    sound = ''.join(song[2:5])

    if sound in dic_song:
        dic_song[sound] = '?'
    else:
        dic_song[sound] = song[1]

for _ in range(m):
    sound = ''.join(input().split())

    if sound in dic_song:
        print(dic_song[sound])
    else:
        print('!')