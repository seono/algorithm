import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

N, L = map(int,input().split())
arr =list(map(int,input().split()))
x = deque([])
ans = []
for i,n in enumerate(arr):
    if x and x[0][1]<=i-L:
        x.popleft()
    while x and x[-1][0]>n:
        x.pop()
    x.append([n,i])
    write('%d '%x[0][0])