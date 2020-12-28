import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
edge = [[] for _ in range(n+1)]
dep = [0]*(n+1)
arr = [[0]*21 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

def LCA(x,y):
    if dep[x]!=dep[y]:
        if dep[x]>dep[y]:x,y=y,x
        for i in range(20,-1,-1):
            if dep[y]-dep[x] >= (1<<i):
                y = arr[y][i]
    if x==y: return x
    for i in range(20,-1,-1):
        if arr[x][i]!=arr[y][i]:
            x = arr[x][i]
            y = arr[y][i]
    return arr[x][0]

def dfs():
    st = [[1,0,0]]
    while st:
        n,d,p = st.pop()
        dep[n]=d
        d+=1
        for i in edge[n]:
            if i==p:continue
            arr[i][0]=n
            st.append([i,d,n])
            
dfs()

for y in range(1,21):
    for x in range(1,n+1):
        arr[x][y]=arr[arr[x][y-1]][y-1]

M = int(input())
for i in range(M):
    x,y = map(int,input().split())
    print(LCA(x,y))