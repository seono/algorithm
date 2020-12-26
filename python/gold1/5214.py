import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int,input().split())
arr = [[] for _ in range(N+M)]
dp = [0]*(N+M)
for idx in range(M):
    temp = list(map(int,input().split()))
    for j in range(K):
        arr[temp[j]-1].append(N+idx)
        arr[N+idx].append(temp[j]-1)
def bfs():
    dp[0]=1
    q = deque([0])
    while q:
        st = q.popleft()
        if st==N-1:
            print(dp[st])
            return
        for nx in arr[st]:
            if not dp[nx]:
                if nx>=N:
                    dp[nx]=dp[st]
                    q.append(nx)
                else:
                    dp[nx]=dp[st]+1
                    q.append(nx)
    print(-1)
    return
bfs()