import sys
input = sys.stdin.readline

n, s, a, b = map(int,input().split())
INF = 1e10
fares = []
tmp = []
for idx,row in enumerate(list(map(str,input().split(',')))):
    row = row.replace("[","").replace("[","")
    row = row.replace("]","").replace("]","")
    if idx>1 and idx%3==0:
        fares.append(tmp)
        tmp = [int(row)]
    else:
        tmp.append(int(row))

adj = [[INF]*(n+1) for _ in range(n+1)]
print(fares)
for c,d,f in fares:
    adj[c][d]=f
    adj[d][c]=f

print("\n".join(map(str,adj)))
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i==j or j==k or i==k:continue
            if adj[i][k]+adj[k][j]<adj[i][j]:
                adj[i][j]=adj[i][k]+adj[k][j]
ans = INF
print("\n".join(map(str,adj)))
for i in range(1,n+1):
    ans = min(ans,adj[s][i]+adj[i][a]+adj[i][b])
print(ans)