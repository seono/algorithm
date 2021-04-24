import sys
import copy
input = sys.stdin.readline

N = int(input())
arr = [[0]*N for _ in range(N)]
ans = N*N
for y in range(N):
    for idx,ch in enumerate(input().strip()):
        if ch=="H":
            arr[y][idx]=1

def check():
    global ans,N
    sum = 0
    for y in range(N):
        tail = 0
        for x in range(N):
            if arr[x][y]:
                tail+=1
        sum+=min(tail,N-tail)
        if sum>ans:
            return sys.maxsize
    return sum

def sol(idx):
    if idx==N:
        return check()
    ret = sys.maxsize
    ret = min(sol(idx+1),ret)
    for y in range(N):
        arr[idx][y]^=1
    ret = min(sol(idx+1),ret)
    for y in range(N):
        arr[idx][y]^=1
    return ret

print(sol(0))