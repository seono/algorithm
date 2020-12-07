import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# down max, right max, left max
arr_d = [0]*M
arr_l = [0]*M
arr_r = [0]*M
arr_d[0]=arr[0][0]
for i in range(1,M):
    arr_d[i]=arr_d[i-1]+arr[0][i]
for i in range(1,N):
    arr_l[0]=arr[i][0]+arr_d[0]
    arr_r[-1]=arr[i][-1]+arr_d[-1]
    for j in range(1,M):
        arr_l[j]=arr[i][j]+max(arr_l[j-1],arr_d[j])
    for j in range(M-2,-1,-1):
        arr_r[j]=arr[i][j]+max(arr_r[j+1],arr_d[j])
    for j in range(0,M):
        arr_d[j]=max(arr_l[j],arr_r[j])
    
print(arr_d[M-1])