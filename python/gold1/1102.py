import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
state = list(input()[:-1])
st_bit = 0
st_cnt = 0
for idx,st in enumerate(state):
    if st=='Y':
        st_cnt+=1
        st_bit = st_bit|1<<idx
p = int(input())
dp_arr = [None]*(1<<16+1)

def dp(cnt, bit):
    if cnt>=p:
        return 0
    if dp_arr[bit] is not None:
        return dp_arr[bit]
    result = 1e9
    for i in range(N):
        if 1<<i & bit:
            for j in range(N):
                if 1<<j & bit:
                    continue
                result = min(dp(cnt+1,bit|1<<j)+arr[i][j], result)
    dp_arr[bit]=result
    return result
if p!=0 and st_bit==0:
    print(-1)
else:
    print(dp(st_cnt,st_bit))
