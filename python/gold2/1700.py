import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
now_list = set()
while len(now_list)<n:
    now_list.add(n_list.pop(0))
now_list = list(now_list)
idx = 0
result = 0
while idx<len(n_list):
    now = n_list[idx]
    idx+=1
    if now in now_list:
        continue
    n_set = set(now_list)
    temp = idx
    while temp<len(n_list) and len(n_set)>1:
        if n_list[temp] in n_set:
            n_set.remove(n_list[temp])
        temp+=1
    re = list(n_set)[0]
    now_list[now_list.index(re)]=now
    result+=1

print(result)