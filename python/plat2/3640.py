import sys
input = sys.stdin.readline

def dfs():
    ret = 0
    while True:
        prev=[-1]*(v+1)
        visited = [False]*(v+1)
        dist = [1e9]*(v+1)
        dist[st]=0
        q = [st]
        visited[st]=True
        while q:
            n = q.pop()
            visited[n]=False
            for nx in adj[n]:
                if cap[n][nx]>fl[n][nx] and dist[nx]>dist[n]+cdj[n][nx]:
                    dist[nx]=dist[n]+cdj[n][nx]
                    prev[nx]=n
                    if not visited[nx]:
                        q.append(nx)
                        visited[nx]=True
        if prev[ed]==-1:break
        flow = 1e9
        now = ed
        while now!=st:
            flow = min(flow,cap[prev[now]][now] - fl[prev[now]][now])
            now = prev[now]
        now = ed
        while now!=st:
            fl[prev[now]][now]+=1
            fl[now][prev[now]]-=1
            ret+=cdj[prev[now]][now]*flow
            now = prev[now]
    return ret

while True:
    try:
        v, e = map(int,input().split())
        st,ed = 0, (v<<1)-1
        tmp = v
        v=v<<1|1
        cap = [[0]*v for _ in range(v)]
        fl = [[0]*v for _ in range(v)]
        adj = [[] for _ in range(v)]
        cdj = [[0]*2001 for _ in range(2001)]
        for i in range(1,tmp+1):
            _in = (i<<1)-2
            _out = (i<<1)-1
            adj[_in].append(_out)
            cap[_in][_out]=1
        cap[0][1]=2
        cap[ed-1][ed]=2
        for _ in range(e):
            a,b,c = map(int,input().split())
            in_a = (a<<1)-2
            out_a = (a<<1)-1
            in_b = (b<<1)-2
            out_b = (b<<1)-1
            cdj[out_a][in_b]=c
            cdj[in_b][out_a]=-c
            adj[out_a].append(in_b)
            adj[in_b].append(out_a)
            cap[out_a][in_b]=1
        print(dfs())
    except:
        break

