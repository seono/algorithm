import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
dx,dy = [0,0,1,-1],[-1,1,0,0]

arr = [[0]*N for _ in range(N)]
u = [[num,1] for num in range(K+1)]
def find(x):
    if u[x][0]!=x:
        u[x][0]=find(u[x][0])
    return u[x][0]

def Union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if u[x][1]<u[y][1]:x,y=y,x
        u[y][0]=x
        u[x][1]+=u[y][1]
    return u[x][1]
def bfs():
    cnt = 0
    while True:
        l = len(st)
        cnt+=1
        flag = False
        while l:
            l-=1
            y,x,p = st.popleft()
            visited[y][x]=1
            for i in range(4):
                ny,nx=y+dy[i],x+dx[i]
                if 0<=ny<N and 0<=nx<N:
                    if arr[ny][nx]:
                        if arr[ny][nx]!=p:
                            if Union(arr[ny][nx],p)==K:
                                flag=True
                                if visited[ny][nx]:
                                    cnt-=1
                    else:
                        st.append([ny,nx,p])
                        arr[ny][nx]=p
        if flag:return cnt

visited = [[0]*N for _ in range(N)]
st = deque()
for num in range(1,K+1):
    x,y = map(int,input().split())
    arr[y-1][x-1]=num
    st.append([y-1,x-1,num])
print(bfs())