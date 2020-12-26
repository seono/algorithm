import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
l_min = sys.maxsize
r_max = 0
for _ in range(n):
    temp = list(map(int,input().split()))
    l_min = min(l_min,min(temp))
    r_max = max(r_max,max(temp))
    arr.append(temp)
l_max = min(arr[0][0],arr[n-1][n-1])
r_min = max(arr[0][0],arr[n-1][n-1])
left = l_min
right = r_min
dy,dx = [0,0,1,-1],[1,-1,0,0]
def bfs():
    st = deque([[0,0]])
    visited = [[False]*n for _ in range(n)]
    while st:
        y,x = st.popleft()
        if y==n-1 and x==n-1:return True
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=n: continue
            if visited[ny][nx]: continue
            if left<=arr[ny][nx]<=right:
                visited[ny][nx]=True
                st.append([ny,nx])
    return False
ans = 1e9
l_flag,r_flag = 0,0
while l_min<=left<=l_max and r_min<=right<=r_max:
    if bfs():
        ans = min(ans,right-left)
        left+=1
        l_flag=1
    else:
        if l_flag and r_flag:
            left+=1
            right+=1
            l_flag=0
            r_flag=0
        else:
            right+=1
            r_flag=1
print(ans)