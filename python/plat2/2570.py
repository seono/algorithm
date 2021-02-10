import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    i,j = map(int,input().split())
    arr[i-1][j-1]=-1
arr1 = [[0]*N for _ in range(N)]
arr2 = [[0]*N for _ in range(N)]
r,l = 1,1

for y in range(N):
    nx = N-1
    ny = y
    flag=False
    while nx>=0 and ny>=0:
        if arr[ny][nx]!=-1:
            if flag:
                flag=False
                l+=1
            arr1[ny][nx]=l
        else:
            flag=True
        ny-=1;nx-=1
    l+=1
for x in range(N-2,-1,-1):
    nx = x
    ny = N-1
    flag=False
    while nx>=0 and ny>=0:
        if arr[ny][nx]!=-1:
            if flag:
                flag=False
                l+=1
            arr1[ny][nx]=l
        else:flag=True
        ny-=1;nx-=1
    l+=1
for y in range(N):
    nx = 0
    ny = y
    flag=False
    while nx<N and ny>=0:
        if arr[ny][nx]!=-1:
            if flag:
                flag=False
                r+=1
            arr2[ny][nx]=r
        else:flag=True
        ny-=1;nx+=1
    r+=1
for x in range(1,N):
    nx = x
    ny = N-1
    flag = False
    while nx<N and ny>=0:
        if arr[ny][nx]!=-1:
            if flag:
                flag=False
                r+=1
            arr2[ny][nx]=r
        else:flag=True
        ny-=1;nx+=1
    r+=1
adj = [[] for _ in range(l)]
for y in range(N):
    for x in range(N):
        if arr[y][x]!=-1:
            adj[arr1[y][x]].append(arr2[y][x])
p = [-1]*r

def dfs(idx):
    if visited[idx]:return False
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or dfs(p[nx]):
            p[nx]=idx
            return True
    return False
ans=0
for i in range(1,l):
    visited = [False]*l
    if dfs(i):
        ans+=1
print(ans)