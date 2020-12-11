import sys
input = sys.stdin.readline

H,W = map(int,input().split())
INF = 1e9
dy,dx = [0,0,1,-1],[1,-1,0,0]
arr = [input()[:-1] for _ in range(H)]
visited = [[[0]*(1<<7) for _ in range(W)]for _ in range(H)]
key_list = 'abcdef'
door_list = 'ABCDEF'
def bfs(y,x):
    st = [[y,x,0]]
    while st:
        ty,tx,c = st.pop(0)
        if arr[ty][tx] == '1':
            return visited[ty][tx][c]
        for i in range(4):
            ny,nx = ty+dy[i],tx+dx[i]
            nk = c
            if ny>=H or ny<0 or nx<0 or nx>=W or arr[ny][nx]=='#':
                continue
            if arr[ny][nx] in door_list:
                if 1<<(ord(arr[ny][nx].lower())-97) & c == 0:
                    continue
            if arr[ny][nx] in key_list:
                nk = c | (1<<(ord(arr[ny][nx])-97))
            if visited[ny][nx][nk]:
                continue
            visited[ny][nx][nk] = visited[ty][tx][c]+1
            st.append([ny,nx,nk])
    return -1
def findST():
    for y in range(H):
        for x in range(W):
            if arr[y][x]=='0':
                return y,x

y,x = findST()
print(bfs(y,x))