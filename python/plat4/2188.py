import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [[]]
for i in range(N):
    arr.append(list(map(int,input().split()[1:])))

p = [None]*201

def sol(idx):
    visited[idx]=True
    for num in arr[idx]:
        if p[num] is None or (not visited[p[num]] and sol(p[num])):
            p[num]=idx
            return True
    return False

ans = 0
for i in range(1,N+1):
    visited = [False]*201
    if sol(i):ans+=1
print(ans)