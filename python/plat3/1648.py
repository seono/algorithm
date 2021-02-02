import sys
input = sys.stdin.readline

mod = 9901

N, M = map(int,input().split())

if (N*M)%2:
    print(0)
    exit(0)
dp_arr = [[-1]*(1<<15) for _ in range(255)]
def dp(board, bit):
    if board==N*M and bit==0:
        return 1
    if board>N*M:
        return 0

    if dp_arr[board][bit]!=-1:
        return dp_arr[board][bit]
    
    if bit&1:
        ret = dp(board+1,bit>>1)
    else:
        ret = dp(board+1,(bit>>1)|1<<(M-1))
        if bit&2==0 and (board%M)!=M-1:
            ret+=dp(board+2,bit>>2)
    dp_arr[board][bit]=ret
    return ret

print(dp(0,0)%mod)