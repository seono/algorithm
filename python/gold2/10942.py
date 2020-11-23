import sys
input = sys.stdin.readline

N = int(input())
arr = [-1] + list(map(int, input().split()))
same_set = {}
def sol(arr1, arr2):
    for i,j in zip(arr1,arr2[::-1]):
        if i!=j:
            return 0
    return 1
M = int(input())
for i in range(M):
    l, r = map(int, input().split())
    if l==r:
        print(1)
        continue
    if (l,r) in same_set:
        print(same_set[l,r])
        continue
    if (l+r)%2==0:
        arr1 = arr[l:int((l+r)/2)]
        arr2 = arr[int((l+r)/2)+1:r+1]
    else:
        arr1 = arr[l:int((l+r)/2)+1]
        arr2 = arr[int((l+r)/2)+1:r+1]
    if sol(arr1,arr2):
        same_set[(l,r)]=1
        while l<r:
            same_set[(l,r)]=1
            l+=1
            r-=1
        print(1)
    else:
        same_set[(l,r)]=0
        print(0)