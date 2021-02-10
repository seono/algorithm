import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
dp_arr = [[-1]*1001 for _ in range(1001)]

def dp(h,i):
    if h==1000 and i==1000:return N
    if i>1000:return N
    if dp_arr[h][i]!=-1:return dp_arr[h][i]
    pt = 1-h+1-i
    cnt = 0
    for need_h, need_i, get_p in arr:
        if need_h>h and need_i>i:continue
        pt+=get_p
        cnt+=1
    if pt==0:
        dp_arr[h][i]=cnt
        return cnt
    ret = cnt
    for j in range(pt+1):
        if h+j>1000:continue
        ret=max(ret,dp(h+j,i+pt-j))
    dp_arr[h][i]=ret
    return ret

print(dp(1,1))