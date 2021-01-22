import sys
input = sys.stdin.readline

N = int(input())

tree = [0]*(200001)
cnt = [0]*(200001)
n = int(input())+1
tmp = n
while tmp<=200000:
    cnt[tmp]+=1
    tree[tmp]+=n
    tmp+=(tmp&-tmp)
ans = 1
total = n
for i in range(1,N):
    n = int(input())+1
    tmp = n
    p=q=0
    while tmp:
        p+=cnt[tmp]
        q+=tree[tmp]
        tmp-=(tmp&-tmp)
    ans *= p*n-q+total-q-(i-p)*n
    ans%=1000000007
    tmp = n
    while tmp<=200000:
        cnt[tmp]+=1
        tree[tmp]+=n
        tmp+=(tmp&-tmp)
    total+=n
print(ans)