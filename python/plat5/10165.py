import sys
input = sys.stdin.readline

N = int(input())

M = int(input())
arr = []
for i in range(M):
    a,b = map(int,input().split())
    if a>b:
        arr.append([a,b+N, i+1])
    else:
        arr.append([a,b,i+1])
        arr.append([a+N,b+N, i+1])

arr.sort(key= lambda x:(x[0],-x[1]))


right = 0
ans_set = set(range(1,M+1))
for st,ed,idx in arr:
    if ed<=right:
        if idx in ans_set:
            ans_set.remove(idx)
    else:
        right = ed
print(' '.join(map(str,list(ans_set))))