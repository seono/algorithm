import sys
input = sys.stdin.readline
output = sys.stdout.write

m = int(input())
arr = list(map(int, input().split()))
LCarr = [[0]*21 for _ in range(m+1)]

for i,num in enumerate(arr,1):
    LCarr[i][0] = num

for y in range(1,21):
    for x in range(1,m+1):
        LCarr[x][y] = LCarr[LCarr[x][y-1]][y-1]

def sol(n,x):
    for i in range(20,-1,-1):
        if n>=1<<i:
            n-=(1<<i)
            x = LCarr[x][i]
    return x


for i in range(int(input())):
    n,x = map(int,input().split())
    output("%d\n"%sol(n,x))