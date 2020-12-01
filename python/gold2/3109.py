import sys
input = sys.stdin.readline

r, c = map(int, input().split())
c_map = [input() for _ in range(r)]

dy,dx = [-1,0,1],[1,1,1]
visited = [[False]*c for _ in range(r)]
result=0
def go(y,x):
    visited[y][x]=True
    if x==c-1:
        return True
    for j in range(3):
        ty,tx = y+dy[j], x+dx[j]
        if ty<0 or ty>=r or visited[ty][tx] or c_map[ty][tx]=='x':
            continue
        if go(ty,tx):
            return True
    return False

for i in range(r):
    if go(i,0):
        result+=1
print(result)
