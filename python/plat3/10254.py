import sys
import math
input = sys.stdin.readline

T = int(input())
def ccw(p1,p2,p3):
    def getD(p1,p2):
        return p2[0] - p1[0], p2[1] - p1[1]
    v,u = getD(p1,p2), getD(p2,p3)
    if v[0] * u[1] > v[1] * u[0]: return True
    return False

def dist(p1,p2):
    return math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2)

def convex(p):
    convex = []
    for p3 in p:
        while len(convex)>=2:
            p1,p2 = convex[-2],convex[-1]
            if ccw(p1,p2,p3):break
            convex.pop()
        convex.append(p3)
    return convex

def rotating_calipers(arr):
    ret = 0
    ans = None
    l = len(arr)-1
    j = 1
    for i in range(l):
        ni = (i+1)%l
        while True:
            nj = (j+1)%l
            vx = arr[ni][0] - arr[i][0]
            vy = arr[ni][1] - arr[i][1]

            ux = arr[nj][0] - arr[j][0]
            uy = arr[nj][1] - arr[j][1]

            tmp = (0,0)

            if ccw(tmp,(vx,vy),(ux,uy)):
                j = nj
            else:break
        tmp = dist(arr[i],arr[j])
        if tmp>ret:
            ans = arr[i]+arr[j]
            ret = tmp
    return ans
while T:
    T-=1
    C = int(input())
    arr = [list(map(int,input().split())) for _ in range(C)]

    arr.sort(key=lambda x:(x[0],x[1]))
    convex_hull = convex(arr)
    arr.reverse()
    tmp = convex(arr)
    convex_hull.extend(tmp[1:])
    print(' '.join(map(str,rotating_calipers(convex_hull))))