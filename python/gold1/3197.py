import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

arr = [list(input()[:-1]) for _ in range(H)]
L_list = []
visit = [[0]*W for _ in range(H)]
dy,dx = [0,0,1,-1],[1,-1,0,0]
que = deque()
for ty in range(H):
    for tx in range(W):
        if arr[ty][tx]=='L':
            L_list.append([ty,tx])
        if visit[ty][tx]:
            continue
        if arr[ty][tx]=='.' or arr[ty][tx]=='L':
            st = [[ty,tx]]
            while st:
                y,x = st.pop(0)
                if arr[y][x]=='X':
                    que.append([y,x])
                    continue
                for i in range(4):
                    ny,nx = y+dy[i],x+dx[i]
                    if ny<0 or ny>=H or nx<0 or nx>=W:
                        continue
                    if visit[ny][nx]:
                        continue
                    visit[ny][nx]=1
                    st.append([ny,nx])
def bfs():
    visited = [[False]*W for _ in range(H)]
    st = deque([L_list[1]])
    ty,tx = L_list[0]
    ans = 0
    global que
    while True:
        temp = []
        while st:
            y,x = st.popleft()
            if y==ty and x==tx:
                return ans
            if arr[y][x]=='X':
                temp.append([y,x])
                continue
            for i in range(4):
                ny,nx = y+dy[i],x+dx[i]
                if ny<0 or ny>=H or nx<0 or nx>=W:
                    continue
                if visited[ny][nx]:
                    continue
                visited[ny][nx]=True
                st.append([ny,nx])
        ans+=1
        st = deque(temp)
        temp = []
        l = len(que)
        while l:
            l-=1
            y,x = que.popleft()
            arr[y][x]='.'
            for i in range(4):
                ny,nx = y+dy[i],x+dx[i]
                if ny<0 or ny>=H or nx<0 or nx>=W:
                    continue
                if arr[ny][nx]=='X' and not visit[ny][nx]:
                    visit[ny][nx]=1
                    que.append([ny,nx])
print(bfs())