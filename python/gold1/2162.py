import sys
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(N)]
group = [1 for i in range(N)]
lineList = []
def findU(x):
    if arr[x]==x:
        return x
    arr[x] = findU(arr[x])
    return arr[x]

def Union(x,y):
    x = findU(x)
    y = findU(y)
    if group[x]>=group[y]:
        arr[y] = x
        group[x]+=group[y]
        return group[x]
    else:
        arr[x] = y
        group[y]+=group[x]
        return group[y]

def ccw(x1,y1,x2,y2,x3,y3):
    tmp1 = (x2-x1)*(y3-y1)
    tmp2 = (y2-y1)*(x3-x1)
    if tmp1==tmp2: return 0
    else:
        if tmp1>tmp2:return 1
        else:return -1

def boundCheck(l1,l2):
    x1,y1,x2,y2=l1
    x3,y3,x4,y4=l2
    def cal(x1,y1,x2,y2):
        return (x1-x2)**2+(y1-y2)**2
    d1 = cal(x1,y1,x2,y2)
    d2 = min(cal(x1,y1,x3,y3),cal(x1,y1,x4,y4))
    d3 = min(cal(x2,y2,x3,y3),cal(x2,y2,x4,y4))
    return d1>=max(d2,d3)

def crossCheck(l1,l2):
    x1,y1,x2,y2 = l1
    x3,y3,x4,y4 = l2
    ck1 = ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)
    if ck1>0: return False
    else:
        ck2 = ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)
        if ck2>0: return False
        elif ck1==0 and ck2==0: return boundCheck(l1,l2) #일직선 상
        else: return True
ans = 1
g_ans = 0
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    lineList.append([x1,y1,x2,y2])
for i in range(N):
    for j in range(i):
        if findU(i)==findU(j):continue
        if crossCheck(lineList[i],lineList[j]):
            ans = max(ans,Union(i,j))
            
for i in range(N):
    if arr[i]==i:
        g_ans+=1
print(g_ans)
print(ans)