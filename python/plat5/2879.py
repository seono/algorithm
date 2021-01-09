import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
p = 0
ans = 0
for num1,num2 in zip(arr1,arr2):
    cnt = num2-num1
    if cnt<0 and p<0:
        if p>cnt:
            ans+=p-cnt
    elif cnt>0 and p>0:
        if p<cnt:
            ans+=cnt-p
    else:
        ans+=abs(cnt)
    p=cnt
print(ans)