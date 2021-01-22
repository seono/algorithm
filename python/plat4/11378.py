import sys

input = sys.stdin.readline
#print = sys.stdout.write

def dfs():
    ans = 0
    while True:
        q = [st]
        flag=False
        visited=[-1]*2050
        while q:
            n = q.pop()

            for nx in adj[n]:
                if cap[n][nx]-fl[n][nx]<=0:continue
                if visited[nx]!=-1:continue
                q.append(nx)
                visited[nx]=n
                if nx==ed:
                    flag = True
                    break
            if flag:break
        if visited[ed]==-1:break
        now = ed
        while now!=st:
            fl[visited[now]][now]+=1
            fl[now][visited[now]]-=1
            now = visited[now]
        ans+=1
    return ans

N, M, K = map(int,input().split())
adj = [[] for _ in range(2050)]
cap = [[0]*2050 for _ in range(2050)]
fl = [[0]*2050 for _ in range(2050)]
st,ed = 0,2021
tmp = 2020
adj[st]=[n for n in range(1,N+1)]+[tmp]
cap[st][tmp]=K
for i in range(N+1,N+M+1):
    cap[i][ed]=1
    adj[i].append(ed)
for i in range(1,N+1):
    row = list(map(int,input().split()))
    adj[i].append(tmp)
    adj[tmp].append(i)
    cap[st][i]=1
    cap[tmp][i]=K
    for num in row[1:]:
        cap[i][num+N]=1
        adj[i].append(num+N)
        adj[num+N].append(i)
        cap[num+N][ed]=1
print("%d\n"%dfs())