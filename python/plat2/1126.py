import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input())
arr = list(map(int,input().split()))
dp_arr = [[-1]*500003 for _ in range(N)]
def dp(idx,n1,n2):
    tmp = n1-n2+250000
    if idx==N:
        return 0 if n1==n2 else -1e9
    if n1>250000 or n2>250000:return -1e9
    if dp_arr[idx][tmp]!=-1:
        return dp_arr[idx][tmp]
    dp_arr[idx][tmp] = dp(idx+1,n1+arr[idx],n2)+arr[idx]
    dp_arr[idx][tmp] = max(dp_arr[idx][tmp],dp(idx+1,n1,n2+arr[idx]),dp(idx+1,n1,n2))
    return dp_arr[idx][tmp]
ans = dp(0,0,0)
if ans:
    print(ans)
else:
    print(-1)