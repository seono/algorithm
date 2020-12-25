import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)
H, W = map(int,input().split())

arr = [list(input()) for _ in range(H)]
cycle = [[False]*W for _ in range(H)]
visited = [[False]*W for _ in range(H)]

visit_list = []

st = [[0,0,0]]
dy,dx = [0,0,-1,1],[1,-1,0,0]
def dfs(y,x):
    global H,W
    p = int(arr[y][x])
    for i in range(4):
        ny,nx = y+dy[i]*p,x+dx[i]*p
        if ny<0 or nx<0 or ny>=H or nx>=W or arr[ny][nx]=='H':
            continue
        if visited[ny][nx]:
            continue
        if cycle[ny][nx]:
            print(-1)
            exit()
        cycle[ny][nx]=True
        dfs(ny,nx)
        cycle[ny][nx]=False
    visited[y][x]=True
    visit_list.append([y,x])
dfs(0,0)
arr2 = [[1]*W for _ in range(H)]
ans = 1
for y,x in visit_list[::-1]:
    p = int(arr[y][x])
    for i in range(4):
        ny,nx = y+dy[i]*p,x+dx[i]*p
        if ny<0 or nx<0 or ny>=H or nx>=W or arr[ny][nx]=='H':
            continue
        arr2[ny][nx]=max(arr2[ny][nx],arr2[y][x]+1)
        ans = max(ans,arr2[ny][nx])
print(ans)