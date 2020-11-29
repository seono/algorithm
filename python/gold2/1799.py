import sys
input = sys.stdin.readline

n = int(input())

ches = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [1,-1,1,-1],[1,1,-1,-1]
right = [[0] * n for _ in range(n)]
left = [[0] * n for _ in range(n)]
r, l = 1,1
for j in range(n):
    i = 0
    while i<n and 0<=j:
        if ches[i][j] == 1:
            right[i][j] = r
        i+=1
        j-=1
    r+=1
for i in range(1,n):
    j = n-1
    while i<n and 0<=j:
        if ches[i][j] == 1:
            right[i][j] = r
        i+=1
        j-=1
    r+=1

for j in range(n-1, -1, -1):
    i = 0
    while i<n and j<n:
        if ches[i][j] == 1:
            left[i][j] = l
        i+=1
        j+=1
    l+=1

for i in range(1,n):
    j = 0
    while i<n and j<n:
        if ches[i][j] == 1:
            left[i][j] = l
        i+=1
        j+=1
    l+=1

link = [[] for _ in range(l)]
for i in range(n):
    for j in range(n):
        if ches[i][j]:
            link[left[i][j]].append(right[i][j])

def dfs(idx):
    visited[idx]=True
    l = link[idx]
    for p in l:
        if r2l[p] == 0 or (not visited[r2l[p]] and dfs(r2l[p])):
            r2l[p] = idx
            l2r[idx] = p
            return True
    return False

l2r = [0] * (2*n)
r2l = [0] * (2*n)
ans = 0
for i in range(1, 2*n):
    if l2r[i]==0:
        visited = [False]*(2*n)
        if dfs(i):
            ans+=1
print(ans)