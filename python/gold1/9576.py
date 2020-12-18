import sys
input = sys.stdin.readline

T = int(input())


def dfs(st):
    if visited[st]:
        return False
    a,b = student[st]
    for i in range(a,b+1):
        if visited[i]:
            continue
        visited[i]=True
        if d[i]==None or dfs(d[i]):
            d[i]=st
            return True
    return False

while T:
    T-=1
    N, M = map(int,input().split())
    d = [None]*(1001)
    ans = 0
    student = []
    for i in range(M):
        a,b = map(int,input().split())
        visited = [False]*(1001)
        student.append([a,b])
        if dfs(i):
            ans+=1
    print(ans)
