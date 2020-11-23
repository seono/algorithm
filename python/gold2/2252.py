import sys
from collections import defaultdict, deque
input = sys.stdin.readline


N, M = map(int, input().split())
f_list = defaultdict(list)
indegree = [0 for i in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    f_list[l].append(r)
    indegree[r]+=1
q = deque([])
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)
results = []
while q:
    n = q.popleft()
    results.append(n)
    for r in f_list[n]:
        indegree[r]-=1
        if indegree[r]==0:
            q.append(r)
print(' '.join(map(str,results)))