import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n = int(input())
arr = []
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    arr.append((x1,y1,y2-1,1))
    arr.append((x2,y1,y2-1,-1))

def update(idx, left, right, start, end, diff):
    if end<left or right<start: return
    #대표 구간 == 범위가 모두 포함되는 곳
    if start<=left and right<=end:
        lazy[idx]+=diff
    else:
        mid = (left+right)//2
        update(idx*2,left,mid,start,end,diff)
        update(idx*2+1,mid+1,right,start,end,diff)
    if lazy[idx]:segTree[idx]=right-left+1
    else:
        if left==right: segTree[idx]=0
        else: segTree[idx]=segTree[idx*2]+segTree[idx*2+1]

arr.sort()
px = arr[0][0]
ans = 0
M_y = 30000
lazy = [0]*(M_y*4)
segTree = [0]*(M_y*4)
for x,y1,y2,check in arr:
    dx = x-px
    px = x
    ans+=dx*segTree[1]
    update(1,0,M_y,y1,y2,check)
print(ans)