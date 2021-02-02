import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
adj = [[] for _ in range(N+1)]
dep = [0]*(N+1)
arr = [[[0,0] for _ in range(21)] for _ in range(N+1)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def LCA(x,y):
    num = 0
    if dep[x]!=dep[y]:
        if dep[x]>dep[y]:x,y=y,x
        for i in range(20,-1,-1):
            if dep[y]-dep[x] >= (1<<i):
                num+=arr[y][i][1]
                y=arr[y][i][0]
    if x==y:return num
    for i in range(20,-1,-1):
        if arr[x][i][0]!=arr[y][i][0]:
            num+=arr[y][i][1]+arr[x][i][1]
            x = arr[x][i][0]
            y = arr[y][i][0]
    return num+arr[x][0][1]+arr[y][0][1]

def LCA2(x,y,k):
    if k==0:return x,True
    num = 0
    if dep[x]!=dep[y]:
        if dep[x]>dep[y]:
            for i in range(20,-1,-1):
                if dep[x]-dep[y]>=(1<<i) and (1<<i)<=k:
                    x=arr[x][i][0]
                    k-=1<<i
                if k==0:
                    return x,True
        else:
            for i in range(20,-1,-1):
                if dep[y]-dep[x]>=1<<i:
                    y=arr[y][i][0]
                    num+=1<<i
    if x==y:
        return num-k,False
    for i in range(20,-1,-1):
        if arr[x][i][0]!=arr[y][i][0] and (1<<i)<=k:
            x = arr[x][i][0]
            y = arr[y][i][0]
            k-=1<<i
            num+=1<<i
        if k==0:
            return x,True
    if k==1:
        return arr[x][0][0],True
    return num-k+2,False

def dfs():
    st = [[1,0,0]]
    while st:
        n, d, p = st.pop()
        dep[n]=d
        d+=1
        for i, cnt in adj[n]:
            if i==p:continue
            arr[i][0]=[n,cnt]
            st.append([i,d,n])
dfs()

for y in range(1,21):
    for x in range(1,N+1):
        arr[x][y][0] = arr[arr[x][y-1][0]][y-1][0]
        arr[x][y][1] += arr[arr[x][y-1][0]][y-1][1]+arr[x][y-1][1]
M = int(input())
for i in range(M):
    row = list(map(int,input().split()))
    if row[0]==1:
        output("%d\n"%LCA(row[1],row[2]))
    else:
        ans,check = LCA2(row[1],row[2],row[3]-1)
        if not check:
            ans,check = LCA2(row[2],row[1],ans)
        output("%d\n"%ans)
