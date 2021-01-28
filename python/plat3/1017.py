import sys
input = sys.stdin.readline

prime_num = [True]*2000
prime_num[0],prime_num[1]=False,False
def getprime():
    next_num = 2
    while next_num<=1000:
        if prime_num[next_num]:
            n = next_num*2
            while n<2000:
                prime_num[n]=False
                n+=next_num
        next_num+=1
getprime()
N = int(input())
arr = list(map(int,input().split()))

#각 숫자끼리 연결시 소수되는 경우 네트워크
#첫번째 숫자와 연결되는 숫자 각각 빼면서 이분탐색

adj = [[] for _ in range(N)]
for idx in range(N-1):
    j = arr[idx]
    for idx2 in range(idx+1,N):
        i = arr[idx2]
        if prime_num[i+j]:
            adj[idx].append(idx2)
            adj[idx2].append(idx)
ans = []
def dfs(idx):
    global n
    visited[idx]=True
    for nx in adj[idx]:
        if nx==n or nx==0:continue
        if p[nx]==-1 or (not visited[p[nx]] and dfs(p[nx])):
            p[nx]=idx
            return True
    return False

for n in adj[0]:
    p = [-1]*N
    #0,n제외
    tmp = 0
    for i in range(1,N):
        visited=[False]*N
        if i==n:continue
        if dfs(i):tmp+=1
    if tmp==N-2:ans.append(arr[n])
if ans:
    print(' '.join(map(str,sorted(ans))))
else:
    print(-1)