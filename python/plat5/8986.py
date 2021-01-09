import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def getdist(k):
    ans = 0
    ans_right = 0
    for idx,num in enumerate(arr[1:],1):
        ans+=abs(idx*k-num)
        ans_right+=abs(idx*(k+1)-num)
    return ans, ans_right

ed = int(1e9)
st = 1
g_mid,g_mid_right=0,0
while st<=ed:
    mid = (st+ed)//2
    g_mid, g_mid_right = getdist(mid)
    if g_mid<g_mid_right:
        ed = mid - 1
    elif g_mid>g_mid_right:
        st = mid + 1
    else:
        break
print(min(g_mid,g_mid_right))