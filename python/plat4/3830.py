import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(x):
    if p[x][0]!=x:
        tmp,weight=find(p[x][0])
        p[x][0]=tmp
        p[x][1]+=weight
    return p[x]

#y는 x보다 w무겁다
def Union(x,y,w):
    #x에서 최상단부모까지 무게
    x,xw = find(x)
    #y에서 최상단부모까지 무게
    y,yw = find(y)
    if x!=y:
        #x에서 최상단까지 무게가 y에서 최상단 무게에 x와 y의 무게차 합보다 작거나 같은경우
        if xw<=yw+w:
            p[x]=[y,yw+w-xw]
        else:
            p[y]=[x,xw-yw-w]

while True:
    N, M = map(int,input().split())
    if N|M==0:break
    p = [(num,0) for num in range(N+1)]
    for i in range(M):
        row = list(input().strip().split())
        if row[0]=="!":
            Union(*map(int,row[1:]))
        else:
            a,b=row[1:]
            a,aw=find(int(a))
            b,bw=find(int(b))
            if a!=b:print("UNKNOWN")
            else:
                print(aw-bw)