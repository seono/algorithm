import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
adj = [[] for _ in range(N)]
for idx,num in enumerate(arr[1:],1):
    adj[num].append(idx)

def dfs(idx):
    ret = 0
    tmp = []
    for num in adj[idx]:
        tmp.append(dfs(num))
    for time,num in enumerate(sorted(tmp,reverse=True),1):
        ret = max(ret,num+time)
    return ret

print(dfs(0))