import sys
from collections import deque
from typing import Deque
input = sys.stdin.readline


N = int(input())
dy = [0,0,1,-1,1,1,-1,-1]
dx = [1,-1,0,0,1,-1,1,-1]

arr = [input() for _ in range(N)]


points = []
ed = []
result_d = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            points.append([i,j])
        elif arr[i][j] =='E':
            ed.append([i,j])
if ed[0][0]==ed[1][0]:
    result_d=1
ey,ex=ed[1]
visit = [[[False,False] for _ in range(N)] for _ in range(N)]
st = deque()
if points[0][0]==points[1][0]:
    st.append(points[1]+[1]+[0])
else:
    st.append(points[1]+[0]+[0])

def check(y,x):
    global N
    for i in range(8):
        ny,nx = y+dy[i],x+dx[i]
        if ny<0 or ny>=N or nx<0 or nx>=N:
            return False
        if arr[ny][nx]=='1':return False
    return True

def sol():
    global ed,st,N
    while st:
        y,x,d,cnt = st.popleft()
        if y==ey and x==ex and d==result_d:
            return cnt
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if d:
                #가로
                if 0<=ny<N and 1<=nx<N-1 and visit[ny][nx][d]==False:
                    if arr[ny][nx-1]!='1' and arr[ny][nx]!='1' and arr[ny][nx+1]!='1':
                        st.append([ny,nx,d,cnt+1])
                        visit[ny][nx][d]=True
            else:
                if 0<=nx<N and 1<=ny<N-1 and visit[ny][nx][d]==False:
                    if arr[ny-1][nx]!='1' and arr[ny][nx]!='1' and arr[ny+1][nx]!='1':
                        st.append([ny,nx,d,cnt+1])
                        visit[ny][nx][d]=True
        if check(y,x):
            if visit[y][x][not d]==False:
                st.append([y,x,not d, cnt+1])
                visit[y][x][not d]=True
    return 0


print(sol())