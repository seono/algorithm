import sys
from collections import defaultdict
input = sys.stdin.readline

H = 2147483647
def hash(x):
    ret = 0
    for c in st[:x]:
        ret=(ret*256+c)%H
    return ret

def rabin(m):
    global L
    mul = (1<<((m-1)*8))%H
    H_x = hash(m)
    H_TABLE[H_x].append(0)
    for idx in range(1,L-m+1):
        H_x = (((H_x - st[idx-1]*mul)<<8) + st[idx+m-1])%H
        for i in H_TABLE[H_x]:
            if st[i:i+m]==st[idx:idx+m]:
                return True
        H_TABLE[H_x].append(idx)
L = int(input())
st = [ord(c)-ord('a') for c in input().strip()]
l,r=1,L-1
while l<=r:
    H_TABLE = defaultdict(list)
    mid = (l+r)>>1
    if rabin(mid):
        l = mid+1
    else:
        r = mid-1
print(r)