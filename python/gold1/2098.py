import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

INF = sys.maxsize
ed = (1<<N)-1
dp = [[None]*(1<<N) for _ in range(N)]

def sol(bit,idx):
    global ed
    if bit==ed:
        return arr[idx][0] or INF
    if dp[idx][bit] is not None:
        return dp[idx][bit]
    tmp = INF
    for next_idx,next_p in enumerate(arr[idx]):
        if bit&1<<next_idx or next_p==0:
            continue
        tmp = min(tmp,sol(bit|(1<<next_idx),next_idx)+next_p)
    dp[idx][bit]=tmp
    return tmp

print(sol(1,0))