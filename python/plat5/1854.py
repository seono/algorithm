import sys
import heapq
input = sys.stdin.readline
output = sys.stdout.write

n, m, k = map(int,input().split())

adj = [[] for _ in range(n+1)]

visited = [[] for _ in range(1001)]
visited[1].append(0)
for _ in range(m):
    a,b,c = map(int,input().split())
    adj[a].append([b,c])

def dijkstra():
    st = [[0,1]]
    while st:
        cnt,p = heapq.heappop(st)
        for nx,ncnt in adj[p]:
            ncnt+=cnt
            if len(visited[nx])<k:
                heapq.heappush(visited[nx],-ncnt)
                heapq.heappush(st,[ncnt,nx])
            elif visited[nx][0]<-ncnt:
                heapq.heappop(visited[nx])
                heapq.heappush(visited[nx],-ncnt)
                heapq.heappush(st,[ncnt,nx])
dijkstra()
for i in range(1,n+1):
    if len(visited[i])!=k:
        output("-1\n")
    else:
        output("%d\n"%-visited[i][0])