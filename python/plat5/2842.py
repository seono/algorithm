import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(l,r):
    st = deque()
    visited = [[False]*(p) for _ in range(p)]
    visited[sty][stx]=True
    st.append([sty,stx])
    while st:
        y,x = st.popleft()
        for i in range(8):
            ny,nx = y+dy[i],x+dx[i]
            if ny<0 or ny>=p or nx<0 or nx>=p:continue
            if visited[ny][nx]:continue
            if l<=arr2[ny][nx]<=r:
                visited[ny][nx]=True
                st.append([ny,nx])
    for y,x in start_list:
        if not visited[y][x]:return False
    return True

p = int(input())
arr = []
start_list = []
for i in range(p):
    temp = list(input().strip())
    for j,t in enumerate(temp):
        if t=='K' or t=='P':
            start_list.append([i,j])
    arr.append(temp)
sty,stx=start_list[0]

arr2 = []

temp_set = set()
for _ in range(p):
    temp = list(map(int,input().split()))
    for t in temp:
        temp_set.add(t)
    arr2.append(temp)

temp_list = sorted(temp_set)
l_min = temp_list[0]
r_max = temp_list[-1]

l_max, r_min = sys.maxsize, 0

for y,x in start_list:
    l_max = min(l_max,arr2[y][x])
    r_min = max(r_min,arr2[y][x])

left_list = []
right_list = []

for k in temp_list:
    if l_min<=k<=l_max:
        left_list.append(k)
    if r_min<=k<=r_max:
        right_list.append(k)

left=right=0
ans = sys.maxsize
l_flag,r_flag = 0,0
while left<len(left_list) and right<len(right_list):
    if bfs(left_list[left],right_list[right]):
        ans = min(ans,right_list[right]-left_list[left])
        left+=1
        l_flag=1
    else:
        if l_flag and r_flag:
            left+=1;right+=1
            l_flag=0
            r_flag=0
        else:
            r_flag=1
            right+=1
print(ans)