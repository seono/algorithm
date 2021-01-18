import sys
input=  sys.stdin.readline

N, K = map(int,input().split())

arr = list(map(int,input().split()))

new_arr = [arr[0]]
for idx in range(1,N):
    if arr[idx]==arr[idx-1]:continue
    new_arr.append(arr[idx])
l = len(new_arr)
dp_arr = [[-1]*l for _ in range(l)]

def sol(st,ed):
    if st==ed:return 0
    if dp_arr[st][ed]!=-1:
        return dp_arr[st][ed]
    res = sys.maxsize
    for i in range(st,ed):
        tmp = 1 if new_arr[st]!=new_arr[i+1] else 0
        res = min(res, sol(st,i)+sol(i+1,ed)+tmp)
    dp_arr[st][ed]=res
    return res
print(sol(0,l-1))