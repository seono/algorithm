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
    if ed<=ped:continue # 돌아가는 거리에 포함되는 사람 제외
    else: 
        if st>ped:
            ans+=(ped-pst)*2
            pst = st
            ped = ed
        else: # 태워서 돌아오는 도착 지점에 딱 뒤로 가는 손님이 있는 경우
            ped = ed
print(ans)