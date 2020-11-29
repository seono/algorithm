import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
st_set = set(range(1,n+1))
for _ in range(m):
    temp = list(map(int, input().split()))
    p = temp[1]
    for t in temp[2:]:
        arr[p].append(t)
        p=t
        indegree[t]+=1
        if t in st_set:
            st_set.remove(t)
st_list = list(st_set)
result = []
while st_list:
    st = st_list.pop(0)
    result.append(st)
    for j in arr[st]:
        indegree[j]-=1
        if indegree[j]==0:
            st_list.append(j)
        elif indegree[j]<0:
            st_list = []
            result = [0]
            break

if len(result)==n:
    print('\n'.join(map(str, result)))
else:
    print(0)

        