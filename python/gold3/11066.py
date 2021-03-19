import sys
input = sys.stdin.readline

T = int(input())


def sol(st,ed):
    if dp_arr[st][ed]!=-1:return dp_arr[st][ed]
    if st==ed:
        return arr[st]
    ret = 1e9
    sum = preSum[ed+1]-preSum[st]
    for i in range(st,ed):
        ret = min(sol(st,i)+sol(i+1,ed)+sum,ret)
    dp_arr[st][ed] = ret
    return ret


while T:
    T-=1
    K = int(input())
    arr = list(map(int,input().split()))
    preSum = [0]*(K+1)
    for i in range(1,K+1):
        preSum[i] = preSum[i-1]+arr[i-1]
    dp_arr = [[-1]*501 for _ in range(501)]
    ans = 1e9
    for i in range(K):
        ans = min(sol(0,i)+sol(i+1,K-1),ans)
    print(ans)
