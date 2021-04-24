import sys
input = sys.stdin.readline
output = sys.stdin.write
N = int(input())

arr = input().strip()

dp_arr = [[-1]*201 for _ in range(201)]

left = "({["
right = ")}]"

mod = 0

def chk(l,r):
    global mod
    if l>r:
        return 1
    if dp_arr[l][r]!=-1:
        return dp_arr[l][r]
    ret = 0
    for i in range(l+1,r+1):
        for k in range(3):
            if arr[l]==left[k] or arr[l]=="?":
                if arr[i]==right[k] or arr[i]=="?":
                    ret+=chk(l+1,i-1)*chk(i+1,r)
                    if ret>=100000:
                        ret%=100000
                        mod = 1
    dp_arr[l][r] = ret
    return ret
ans = chk(0,N-1)
if ans == 0: print (ans)
elif mod: print(str(ans).zfill(5))
else: print(ans)