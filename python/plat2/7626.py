import sys
import bisect
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n = int(input())
arr = []
M_y = 200000
lenT = [0]*(M_y*4)
tmp = []
for _ in range(n):
    x1,x2,y1,y2 = map(int,input().split())
    arr.append([x1,y1,y2,1])
    arr.append([x2,y1,y2,-1])
    tmp.append(y1)
    tmp.append(y2)

tmp = sorted(set(tmp))
M = len(tmp)
for i in range(M-1):
    lenT[i+M] = tmp[i+1]-tmp[i]
for i in range(M-1,0,-1):
    lenT[i] = lenT[i<<1]+lenT[i<<1 | 1]

def update(left, right, diff):
    def apply(i,v):
        lazy[i]+=v
        segTree[i]=lenT[i] if lazy[i] else segTree[i<<1]+segTree[i<<1|1] if i<M else 0

    start,end = left,right
    while left!=right:
        if left & 1:
            apply(left,diff)
            left+=1
        if right & 1:
            right-=1
            apply(right,diff)
        left>>=1;right>>=1;
    segTree[start] = lenT[start] if lazy[start] else 0
    segTree[end] = lenT[end] if lazy[end] else 0
    idx = end>>1
    while idx:
        segTree[idx]=lenT[idx] if lazy[idx] else segTree[idx<<1]+segTree[idx<<1|1]
        idx>>=1
    idx = start>>1
    while idx:
        segTree[idx]=lenT[idx] if lazy[idx] else segTree[idx<<1]+segTree[idx<<1|1]
        idx>>=1
arr.sort()
px = arr[0][0]
ans = 0
lazy = [0]*(M_y*4)
segTree = [0]*(M_y*4)
for i in range(2*n):
    arr[i][1] = bisect.bisect_left(tmp,arr[i][1])+M
    arr[i][2] = bisect.bisect_left(tmp,arr[i][2])+M

for x,y1,y2,check in arr:
    dx = x-px
    px = x
    ans+=dx*segTree[1]
    update(y1,y2,check)
print(ans)