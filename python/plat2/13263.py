import sys
input = sys.stdin.readline
output = sys.stdout.write

class Line(object):
    def __init__(self,p,c):
        self.p = p
        self.c = c
        self.s = 0

def cross(l1,l2):
    return (l1.c-l2.c)/(l2.p-l1.p)

n = int(input())
tree_height = list(map(int,input().split()))
tree_p = list(map(int,input().split()))
dp_arr = [-1]*(n+1)
dp_arr[0] = 0
st = [None]*(n+1)
top = 0

for i in range(1,n):
    l = Line(tree_p[i-1],dp_arr[i-1])
    while top>0:
        l.s = cross(st[top-1],l)
        if st[top-1].s<l.s: break;
        top-=1
    st[top] = l
    top+=1
    x = tree_height[i]
    idx = top-1
    if x<st[idx].s:
        l,r = 0,idx
        while l+1<r:
            mid = (l+r)>>1
            if x<st[mid].s:
                r = mid
            else:
                l = mid
        idx = l
    dp_arr[i] = st[idx].p*x + st[idx].c
print(dp_arr[n-1])