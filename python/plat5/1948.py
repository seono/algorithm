import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adj_f = [[] for _ in range(n+1)]
adj_b = [[] for _ in range(n+1)]
visited = [False]*(n+1)
indegree = [0]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    adj_f[a].append([b,c])
    adj_b[b].append([a,c])
    indegree[b]+=1
dist = [0]*(n+1)

start,end = map(int,input().split())

st = [start]
while st:
    n = st.pop()
    for nx, c in adj_f[n]:
        if dist[nx]<dist[n]+c:
            dist[nx]=dist[n]+c
        indegree[nx]-=1
        if indegree[nx]==0:
            st.append(nx)
ans = 0
print(dist[end])
st = [end]
while st:
    n = st.pop()
    dis = dist[n]
    for i,c in adj_b[n]:
        if dis == dist[i]+c:
            ans+=1
            if not visited[i]:
                visited[i]=True
                st.append(i)
print(ans)