import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
while T:
    T-=1
    N, L, K = map(int,input().split())
    left,right = [],[]
    id_list = []
    for _ in range(N):
        p, id = map(int,input().split())
        id_list.append(id)
        if id<0:
            left.append(p)
        else:
            right.append(L-p)
    ans = []
    for idx,l in enumerate(left):
        ans.append([l,id_list[idx]])
    for idx,r in enumerate(right,len(ans)):
        ans.append([r,id_list[idx]])
    ans.sort(key=lambda x:(x[0],x[1]))
    print(ans[K-1][1])