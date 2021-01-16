import sys
input = sys.stdin.readline

N , M = map(int,input().split())
p = [None]*(M+1)
arr = []
for _ in range(N):
    row = list(map(int,input().split()))[1:]
    arr.append(row)
    arr.append(row)
def sol(idx):
    visited[idx]=True
    for nx in arr[idx]:
        if p[nx]==None or (not visited[p[nx]] and sol(p[nx])):
            p[nx]=idx
            return True
    return False
ans = 0
for i in range(N*2):
    visited = [False]*(N*2)
    if sol(i):ans+=1
print(ans)
