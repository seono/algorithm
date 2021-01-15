import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
for i in range(N):
    start,end = map(int,input().split())
    if start<end:continue
    arr.append([end,start])
arr.sort()
ped = arr[0][1]
ans = M
pst = arr[0][0]
arr.append([1e9+1,1e9+1])
for st,ed in arr:
    if ed<=ped:continue
    else:
        if st>ped:
            ans+=(ped-pst)*2
            pst = st
            ped = ed
        else:
            ped = ed
print(ans)