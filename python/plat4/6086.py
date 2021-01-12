import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cap = [[0]*52 for _ in range(52)]
fl = [[0]*52 for _ in range(52)]
adj = [[] for _ in range(52)]
for _ in range(N):
    a,b,c=input().strip().split()
    a = ord(a)-ord('A')
    b = ord(b)-ord('A')
    if a>25:
        a = a-6
    if b>25:
        b = b-6
    c=int(c)
    cap[a][b]+=c
    cap[b][a]+=c
    adj[a].append(b)
    adj[b].append(a)

def bfs(st,ed):
    ans = 0
    while True:
        visited = [-1]*52

        q = deque([st])

        while q:
            n = q.popleft()

            for nx in adj[n]:
                if cap[n][nx]-fl[n][nx]<=0:continue
                if visited[nx]!=-1:continue

                q.append(nx)
                visited[nx]=n
                if nx==ed:break
        if visited[ed]==-1:break

        flow = sys.maxsize
        now = ed
        while now!=st:
            flow = min(flow, cap[visited[now]][now] - fl[visited[now]][now])
            now = visited[now]
        now = ed
        while now!=st:
            fl[visited[now]][now]+=flow
            fl[now][visited[now]]-=flow
            now = visited[now]
        ans+=flow
    return ans


print(bfs(0,25))