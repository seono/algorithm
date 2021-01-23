import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
d = [(-1,0),(0,1),(1,0),(0,-1)]

arr = [[0]*N for _ in range(N)]
u = [num for num in range(K+1)]

def find(x):
    if u[x]!=x:
        u[x]=find(u[x])
    return u[x]

def bfs():
    global K
    cnt = 0
    while st:
        for y,x in st:
            cur = arr[y][x]
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
                    near = arr[ny][nx]
                    cur_root = find(cur)
                    near_root = find(near)
                    if cur_root==near_root:continue
                    K-=1
                    if cur_root<near_root:
                        u[near_root] = cur_root
                    else:
                        u[cur_root] = near_root
        if K==1:
            return cnt
        cnt+=1
        l = len(st)
        while l:
            l-=1
            y,x = st.popleft()
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<N and arr[ny][nx]==0:
                    st.append((ny,nx))
                    arr[ny][nx]=arr[y][x]
    return cnt

st = deque()
for num in range(K):
    x,y = map(int,input().split())
    arr[y-1][x-1]=num+1
    st.append((y-1,x-1))
print(bfs())