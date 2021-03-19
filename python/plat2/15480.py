import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

depth = [0]*(N+1)
arr = [[0]*21 for _ in range(N+1)]
def dfs(idx):
    st = [idx]
    depth[idx]=1
    while st:
        now = st.pop()
        for nxt in adj[now]:
            if depth[nxt]: continue
            arr[nxt][0]=now
            depth[nxt]=depth[now]+1
            st.append(nxt)
dfs(1)

for y in range(1,21):
    for x in range(1,N+1):
        arr[x][y] = arr[arr[x][y-1]][y-1]
def LCA(x,y):
    if depth[x]!=depth[y]:
        if depth[x]>depth[y]:x,y=y,x
        for i in range(20,-1,-1):
            if depth[y]-depth[x]>=(1<<i):
                y=arr[y][i]
    if x==y: return x
    for i in range(20,-1,-1):
        if arr[x][i]!=arr[y][i]:
            x = arr[x][i]
            y = arr[y][i]
    return arr[x][0]

for _ in range(int(input())):
    r, u, v = map(int,input().split())
    ans = LCA(r,u)
    tmp = LCA(u,v)
    ans = ans if depth[ans]>=depth[tmp] else tmp
    tmp = LCA(r,v)
    ans = ans if depth[ans]>=depth[tmp] else tmp
    print(ans)
