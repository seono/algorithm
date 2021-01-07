import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int,input().split())

arr = list(map(int,input().split()))

window = deque()
L = 2*M-1
for idx,light in enumerate(arr):
    if window and window[0][1]<=idx-L:
        window.popleft()
    while window and window[-1][0]<light:
        window.pop()
    window.append([light,idx])
    if idx>=L-1:
        output("%d "%window[0][0])