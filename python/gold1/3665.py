import sys
input = sys.stdin.readline
T = int(input())
n = 0
def topo():
    start = 0
    global n
    ans = []
    for i in range(1,n+1):
        if degree[i]==0:
            if start:
                print("?")
                return
            start = i
            ans.append(start)

    while len(arr[start])>0:
        next = start
        start = 0
        for x in arr[next]:
            degree[x]-=1
            if degree[x]==0:
                if start:
                    print("?")
                    return
                start = x
                ans.append(start)
    if len(ans)==n:
        print(" ".join(map(str,ans)))
    else:
        print("IMPOSSIBLE")
    return

while T:
    T-=1
    n = int(input())
    temp = list(map(int,input().split()))
    degree = [0]*(n+1)
    arr = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1,n):
            arr[temp[i]].append(temp[j])
            degree[temp[j]]+=1
    m = int(input())
    check=False
    n_arr = arr[:]
    for _ in range(m):
        a,b = map(int,input().split())
        if a in arr[b]:
            idx = arr[b].index(a)
            arr[b].pop(idx)
            degree[a]-=1
            degree[b]+=1
            arr[a].append(b)
        elif b in arr[a]:
            idx = arr[a].index(b)
            arr[a].pop(idx)
            degree[b]-=1
            degree[a]+=1
            arr[b].append(a)
    topo()