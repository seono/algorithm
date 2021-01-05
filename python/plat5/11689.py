import sys
input = sys.stdin.readline

k = int(input())

i = 2
ans = k
while i*i<=k:
    if k % i ==0:
        while k % i == 0:
            k//=i
        ans = ans//i*(i-1)
    i+=1
if k!=1:
    ans = ans//k*(k-1)
print(ans)