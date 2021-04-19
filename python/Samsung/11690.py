import sys
import bisect

sys.stdin = open("input.txt", "r")
N,L = 0,0
arr = []

def getSub(subList):
    temp = [0]*21
    s = 0
    for num in subList:
        t = temp[num]
        temp[num] += s+1-t
        s += s+1-t
    return s

def checkLIS(LIS):
    l = [LIS[0]]
    if L==1:return True
    for num in LIS[1:]:
        idx = bisect.bisect_left(l,num)
        if idx==len(l):
            l.append(num)
            if len(l)==L: return True
        else:
            l[idx]=num
    return False


def sol(LIS,idx):
    global temp
    l = len(LIS)
    if LIS in temp[idx]:
        return 0
    temp[idx].append(LIS)
    if l>=L and checkLIS(LIS):
        return getSub(arr[idx:])+1
    if idx==N: return 0
    num = arr[idx]
    return sol(LIS+[num],idx+1) + sol(LIS,idx+1)
            
T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = list(map(int,input().split()))
    temp = [[] for _ in range(N+1)]
    if checkLIS(arr):
        if L==1:
            print("#"+str(test_case),getSub(arr))
        else:
            print("#"+str(test_case),sol([],0))
    else:
        print("#"+str(test_case),0)
    print(temp)