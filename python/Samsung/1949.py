import sys
sys.stdin = open("input.txt", "r")

d=[(0,1),(1,0),(-1,0),(0,-1)]

def getHighest():
    global N
    ret = []
    hi = -1e10
    for y in range(N):
        for x in range(N):
            if arr[y][x]>hi:
                ret = [(y,x)]
                hi = arr[y][x]
            elif arr[y][x]==hi:
                ret.append((y,x))
    return ret

def dfs(y,x):
    global N
    visited = [[0]*N for _ in range(N)]
    visited[y][x] = 1
    st = [(y,x,1)]
    ret = 0
    while st:
        y,x,l = st.pop()
        ret = max(ret,l)
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if ny<0 or ny>=N or nx<0 or nx>=N or visited[ny][nx]>=l: continue
            if arr[ny][nx]<arr[y][x]:
                st.append((ny,nx,l+1))
                visited[ny][nx]=l+1
    return ret

def sol():
    global K,N
    ans = 1
    h_list = getHighest()
    for y in range(N):
        for x in range(N):
            for i in range(1,K+1):
                arr[y][x]-=i
                for ty,tx in h_list:
                    ans = max(ans,dfs(ty,tx))
                arr[y][x]+=i
    return ans

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print("#"+str(test_case),sol())
