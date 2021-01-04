import sys
import heapq
input = sys.stdin.readline

while True:
    N, M = map(int,input().split())
    if N==0 and M==0:break
    start, end = map(int,input().split())

    adj_f = [[] for _ in range(N+1)]
    adj_b = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        adj_f[a].append([b,c])
        adj_b[b].append([a,c])
    st = [[0,start]]
    dist = [sys.maxsize]*(N+1)
    dist[start]=0
    ans = 0
    while st:
        dis, n = heapq.heappop(st)
        for i,c in adj_f[n]:
            if dist[i]>dist[n]+c:
                dist[i]=dist[n]+c
                heapq.heappush(st,[dist[i],i])
    st = [end]
    visited = [False]*(N+1)
    while st:
        n = st.pop()
        for i,c in adj_b[n]:
            if dist[n]==dist[i]+c:
                for idx in range(len(adj_f[i])):
                    if adj_f[i][idx][0]==n:
                        adj_f[i].pop(idx)
                        break
                if not visited[i]:
                    visited[i]=True
                    st.append(i)
    dist = [sys.maxsize]*(N+1)
    dist[start] = 0
    st = [[0,start]]
    while st:
        dis, n = heapq.heappop(st)
        for i,c in adj_f[n]:
            if dist[i]>dist[n]+c:
                dist[i]=dist[n]+c
                heapq.heappush(st,[dist[i],i])
    print(dist[end] if dist[end]!=sys.maxsize else -1)