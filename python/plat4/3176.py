import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
edge = [[] for _ in range(N+1)]
dep = [0]*(N+1)
arr = [[[0,sys.maxsize,0] for _ in range(21)] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))

def LCA(x,y):
    num_min,num_max = sys.maxsize,0
    if dep[x]!=dep[y]:
        if dep[x]>dep[y]:x,y=y,x
        for i in range(20,-1,-1):
            if dep[y]-dep[x] >= (1<<i):
                num_min = min(num_min,arr[y][i][1])
                num_max = max(num_max,arr[y][i][2])
                y = arr[y][i][0]
    if x==y: return num_min,num_max
    for i in range(20,-1,-1):
        if arr[x][i][0]!=arr[y][i][0]:
            num_min = min(num_min,arr[x][i][1],arr[y][i][1])
            num_max = max(num_max,arr[x][i][2],arr[y][i][2])
            x = arr[x][i][0]
            y = arr[y][i][0]
            pass
    return min(num_min,arr[x][0][1],arr[y][0][1]),max(num_max,arr[x][0][2],arr[y][0][2])

def dfs():
    st = [[1,0,0]]
    while st:
        n, d, p = st.pop()
        dep[n]=d
        d+=1
        for i,cnt in edge[n]:
            if i==p:continue
            arr[i][0]=[n,cnt,cnt]
            st.append([i,d,n])
dfs()

for y in range(1,21):
    for x in range(1,N+1):
        arr[x][y][0]=arr[arr[x][y-1][0]][y-1][0]
        arr[x][y][1]=min(arr[arr[x][y-1][0]][y-1][1],arr[x][y-1][1])
        arr[x][y][2]=max(arr[arr[x][y-1][0]][y-1][2],arr[x][y-1][2])

M = int(input())
for i in range(M):
    x,y = map(int,input().split())
    print("%d %d\n"%(LCA(x,y)))