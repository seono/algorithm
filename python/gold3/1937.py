import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

d = [(0,1),(1,0),(-1,0),(0,-1)]

dp_arr = [[-1]*N for _ in range(N)]

def sol(y,x):
    if dp_arr[y][x]!=-1: return dp_arr[y][x]
    ret = 1
    for dy,dx in d:
        ny,nx = dy+y, dx+x
        if ny<0 or ny>=N or nx<0 or nx>=N:continue
        if arr[ny][nx]>arr[y][x]:
            ret = max(sol(ny,nx)+1,ret)
    dp_arr[y][x] = ret
    return ret
ans = 0
for i in range(N):
    for j in range(N):
        ans=max(ans,sol(i,j))
print(ans)