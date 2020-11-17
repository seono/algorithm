import sys
input = sys.stdin.readline

from collections import defaultdict

#아무 노드에서 출발
#갈림길 생가면 해당 점에서 모든 루트 계산(재귀)
#가장 먼거리 선택

g=defaultdict(list)
visited=[]


def sol(idx, p):
    next_list = g[idx][:]
    visited[idx] = 1
    max_p = p
    max_idx = idx
    while next_list:
        n_idx, c = next_list.pop()
        if visited[n_idx]!=-1:
            continue
        visited[n_idx]=1
        temp_p, idx = sol(n_idx,p+c)
        if temp_p >max_p:
            max_p = temp_p
            max_idx = idx
    return max_p, max_idx
    

if __name__ == "__main__":
    N = int(input())
    for _ in range(N+1):
        visited.append(-1)
    for i in range(1,N+1):
        d = list(map(int, input().split(' ')))
        target = d[0]
        d = d[1:-1]
        for x in range(int(len(d)/2)):
            g[target].append([d[x*2],d[x*2+1]])
    #print(g)
    p, start_idx = sol(1,0)
    for i in range(N+1):
        visited[i] = -1
    p, end_idx = sol(start_idx,0)
    print(p)
    