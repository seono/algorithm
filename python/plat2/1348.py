import sys
from collections import defaultdict
input = sys.stdin.readline

R, C = map(int,input().split())

arr = [list(input().strip()) for _ in range(R)]

d = [(0,1),(1,0),(0,-1),(-1,0)]
N = 201
adj = [[] for _ in range(N)]
dist = [[0]*N for _ in range(N)]
car_num,park_num = 1,101
for i in range(R):
    for j in range(C):
        if arr[i][j]=='C':
            arr[i][j]=car_num
            car_num+=1
        elif arr[i][j]=='P':
            arr[i][j]=park_num
            park_num+=1
        elif arr[i][j]=='X':
            arr[i][j] = -1
        else:
            arr[i][j] = 0
if car_num==1:
    print(0)
    exit(0)
if car_num+100>park_num:
    print(-1)
    exit(0)
max_T = 0
def bfs(y,x):
    global max_T
    visited = [[False]*C for _ in range(R)]
    q= [(y,x)]
    visited[y][x]=True
    lv = 0
    now_car = arr[y][x]
    while q:
        length = len(q)
        while length:
            length-=1
            ny,nx = q.pop(0)
            if 100<arr[ny][nx]:
                now_park = arr[ny][nx]
                adj[now_car].append(now_park)
                dist[now_car][now_park]=lv
                max_T=max(lv, max_T)
            for dy,dx in d:
                ty,tx = ny+dy,nx+dx
                if ty<0 or ty>=R or tx<0 or tx>=C:continue
                if visited[ty][tx]:continue
                if arr[ty][tx]==-1:continue
                visited[ty][tx]=True
                q.append((ty,tx))
        lv+=1


for i in range(R):
    for j in range(C):
        if 0<arr[i][j]<101:
            bfs(i,j)
def sol():
    ans = 0
    p = [None]*N
    def dfs(idx,T):
        if visited[idx]:return False
        visited[idx]=True
        for nx in adj[idx]:
            if(dist[idx][nx]>T):continue
            if p[nx] is None or dfs(p[nx],T):
                p[nx]=idx
                return True
        return False
    for i in range(1,car_num):
        visited = [False]*N
        if dfs(i,max_T):ans+=1
    return ans==car_num-1

ans = -1
l,r = 0, 5001
while l<=r:
    max_T = (l+r)>>1
    if sol():
        ans = max_T
        r = max_T-1
    else:
        l = max_T+1
print(ans)