import sys
input = sys.stdin.readline

K = int(input())
chu_list = list(map(int, input().split()))
N = int(input())
g_list = list(map(int,input().split()))

num_set = set(chu_list)

visited = [[-1 for _ in range(65001)] for _ in range(K)]

def sol(num_idx,l,r):
    if l==r:
        return 1
    if len(chu_list)==num_idx:
        return 0
    if visited[num_idx][abs(l-r)]!=-1:
        return visited[num_idx][abs(l-r)]
    w = chu_list[num_idx]
    result = sol(num_idx+1,l+w,r) or sol(num_idx+1,l,r+w) or sol(num_idx+1, l, r)    
    visited[num_idx][abs(l-r)] = result
    return result
result = []
for i in range(N):
    if sol(0,g_list[i],0):
        result.append('Y')
    else:
        result.append('N')
print(' '.join(map(str, result)))