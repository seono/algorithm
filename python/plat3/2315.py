import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int,input().split())

dp_arr = [[[1e10,1e10] for _ in range(1003)] for _ in range(1003)]

arr = [0]
sum = [0]*1010
for i in range(1,N+1):
    idx, cost=map(int,input().split())
    arr.append(idx)
    sum[i]=sum[i-1]+cost
arr.append(1000)
def dp(l,r,flag):
    if l==1 and r==N:return 0
    if dp_arr[l][r][flag]!=1e10:
        return dp_arr[l][r][flag]

    now = l if flag else r
    #l로 가서 가로등 끔
    time = sum[N] - sum[r] + sum[l-1]
    if l>1:
        dp_arr[l][r][flag] = min(dp_arr[l][r][flag],dp(l-1,r,1)+(arr[now]-arr[l-1])*time)
    #r로 가서 가로등 끔
    if r<N:
        dp_arr[l][r][flag] = min(dp_arr[l][r][flag],dp(l,r+1,0)+(arr[r+1]-arr[now])*time)
    return dp_arr[l][r][flag]
print(dp(M,M,0))