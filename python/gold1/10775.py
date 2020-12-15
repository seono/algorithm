import sys
input = sys.stdin.readline

G = int(input())
arr = [None]*(G+1)
arr[0]=-1
P = int(input())
result = 0
P_list = []
for _ in range(P):
    P_list.append(int(input()))
for gi in P_list:
    idx = gi
    while idx>-1 and arr[idx] is not None:
        idx = arr[idx]
    if idx==-1:
        break
    arr[idx]=arr[gi]=idx-1
    result+=1
print(result)