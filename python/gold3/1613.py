import sys
input = sys.stdin.readline

def sol(arr):
    N = len(arr)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][k] and arr[k][j]:
                    arr[i][j]=1
    return arr
N, K = map(int, input().split())
arr = [[0]*N for i in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
s = int(input())
answer_list = sol(arr)
answer = []
for _ in range(s):
    i, j = map(int, input().split())
    if(answer_list[i-1][j-1] == 1):
        answer.append(-1)
    elif(answer_list[j-1][i-1] == 1):
        answer.append(1)
    else:
        answer.append(0)

print('\n'.join(map(str,answer)))