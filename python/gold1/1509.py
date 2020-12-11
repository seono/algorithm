import sys
input = sys.stdin.readline

dp = [[False]*2501 for _ in range(2501)]

arr = input()[:-1]
n = len(arr)
for i in range(n+1):
    dp[i][i]=True
for i in range(n-1):
    if arr[i]==arr[i+1]:
        dp[i][i+1]=True
for k in range(2,n):
    for j in range(n-k):
        i = j+k
        if arr[i]==arr[j] and dp[j+1][i-1]:
            dp[j][i]=True
dp2 = [None]*2501
def check2(s):
    if s==len(arr):
        dp2[s]=0
        return 0
    result = len(arr)
    if dp2[s] is not None:
        return dp2[s]
    for j in range(len(arr)-1,s-1,-1):
        if dp[s][j]:
            result = min(result,1+check2(j+1))
    dp2[s]=result
    return result
sys.setrecursionlimit(3000)
print(check2(0))
