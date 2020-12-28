import sys
input = sys.stdin.readline
V, E = map(int,input().split())

arr_f = [[] for _ in range(V+1)]
arr_b = [[] for _ in range(V+1)]

for _ in range(E):
    a,b=map(int,input().split())
    arr_f[a].append(b)
    arr_b[b].append(a)
visited = [False]*(V+1)
st = []
ans = []
ans_idx = 0
sys.setrecursionlimit(100001)
def dfs(idx):
    visited[idx]=True
    for n in arr_f[idx]:
        if visited[n]:continue
        dfs(n)
    st.append(idx)

def b_dfs(idx):
    visited[idx]=True
    ans[ans_idx].append(idx)
    for n in arr_b[idx]:
        if visited[n]:continue
        b_dfs(n)

for i in range(1,V+1):
    if visited[i]:continue
    dfs(i)

visited = [0]*(V+1)

while st:
    n = st.pop()
    if visited[n]:continue
    ans.append([])
    b_dfs(n)
    ans_idx+=1
print(ans_idx)
for i in range(ans_idx):
    ans[i].sort()
ans.sort()
for i in ans:
    print(' '.join(map(str,i+[-1])))