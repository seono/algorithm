import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
dy,dx = [0,0,1,-1],[1,-1,0,0]
def sol():
    h,w = map(int, input().split())
    arr = []
    visited = [[0]*(w+2) for _ in range(h+2)]
    arr.append('.'*(w+2))
    for _ in range(h):
        arr.append('.'+input().strip()+'.')
    arr.append('.'*(w+2))
    key_list = input().strip()
    if key_list=='0':
        key_list=""
    ans=0
    st = defaultdict(list)
    q = [[0,0]]
    visited[0][0]=1
    while q:
        y,x = q.pop(0)
        if 0<=ord(arr[y][x])-ord('A')<26:
            if arr[y][x].lower() not in key_list:
                st[arr[y][x].lower()].append([y,x])
                continue
        if 0<=ord(arr[y][x])-ord('a')<26:
            if arr[y][x] not in key_list:
                key_list=key_list+arr[y][x]
                for n in st[arr[y][x]]:
                    q.append(n)
        elif arr[y][x]=='$':
            ans+=1
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ny>h+1 or nx>w+1 or nx<0 or ny<0:
                continue
            if visited[ny][nx] or arr[ny][nx]=='*':
                continue
            visited[ny][nx]=1
            q.append([ny,nx])
    return ans
for _ in range(T):
    print(sol())