import sys
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int,input().split())
tree = [[0]*(N+1) for _ in range(N+1)]
arr = []
def update(y,x,n):
    while y<=N:
        temp = x
        while temp<=N:
            tree[y][temp]+=n
            temp+=(temp&-temp)
        y+=(y&-y)

def get(y1,x1,y2,x2):
    def getIdx(x,y):
        ans = 0
        while y>0:
            temp = x
            while temp>0:
                ans+=tree[y][temp]
                temp-=(temp&-temp)
            y-=(y&-y)
        return ans
    return getIdx(x2,y2)+getIdx(x1-1,y1-1)-getIdx(x1-1,y2)-getIdx(x2,y1-1)

for y in range(N):
    row = list(map(int,input().split()))
    for x in range(N):
        update(y+1,x+1,row[x])
    arr.append(row)
for _ in range(M):
    row = list(map(int,input().split()))
    if row[0]==0:
        update(row[1],row[2],row[3]-arr[row[1]-1][row[2]-1])
        arr[row[1]-1][row[2]-1]= row[3]
    else:
        x1,y1 = row[1],row[2]
        x2,y2 = row[3],row[4]
        if x1>x2:x1,x2=x2,x1
        if y1>y2:y1,y2=y2,y1
        output("%d\n"%get(x1,y1,x2,y2))
