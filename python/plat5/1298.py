import sys
input = sys.stdin.readline

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
selected = [0]*(N+1)
visited = [False]*(N+1)

def select(a):
    if visited[a]:return False
    visited[a]=True
    for n in adj[a]:
        if selected[n] == 0 or select(selected[n]):
            selected[n]=a
            return True
    return False
ans = 0
for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)

for i in range(1,N+1):
    visited = [False]*(5001)
    if select(i):ans+=1
print(ans)