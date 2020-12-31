import sys
input = sys.stdin.readline

n = int(input())
edge = [[] for _ in range(n+1)]
dep = [0]*(n+1)
arr = [[[0,0] for _ in range(21)] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    edge[a].append([b,c])
    edge[b].append([a,c])

def LCA(x,y):
    ans = 0
    if dep[x]!=dep[y]:
        if dep[x]>dep[y]:x,y=y,x
        for i in range(20,-1,-1):
            if dep[y]-dep[x] >= (1<<i):
                ans+=arr[y][i][1]
                y = arr[y][i][0]
    if x==y: return ans
    for i in range(20,-1,-1):
        if arr[x][i][0]!=arr[y][i][0]:
            ans+=arr[x][i][1]
            x = arr[x][i][0]
            ans+=arr[y][i][1]
            y = arr[y][i][0]
    return ans+arr[x][0][1]+arr[y][0][1]

def dfs():
    st = [[1,0,0]]
    while st:
        n,d,p = st.pop()
        dep[n]=d
        d+=1
        for i,cnt in edge[n]:
            if i==p:continue
            arr[i][0]=[n,cnt]
            st.append([i,d,n])
            
dfs()

for y in range(1,21):
    for x in range(1,n+1):
        arr[x][y][0]=arr[arr[x][y-1][0]][y-1][0]
        arr[x][y][1]=arr[arr[x][y-1][0]][y-1][1]+arr[x][y-1][1]

M = int(input())
for i in range(M):
    x,y = map(int,input().split())
    print(LCA(x,y))