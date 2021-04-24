import sys
sys.stdin = open("input.txt", "r")

D,W,K,ret = 0,0,0,0

def check():
    global D,W,K
    for w in range(W):
        aflag = 0
        bflag = 0
        flag = False
        for i in range(D):
            if (arr[w]>>i)&1:
                aflag+=1
                bflag = 0
            else:
                bflag+=1
                aflag = 0
            if aflag==K or bflag==K: 
                flag = True
                break
        if not flag:
            return False
    return True

def sol(idx,k):
    global D,W,K,ret
    if k>K: return K
    if k and check():
        return k
    if idx==D:
        return 100
    ret = min(ret,sol(idx+1,k))
    temp = 0
    #1로 통합
    for w in range(W):
        temp<<=1
        temp|=((arr[w]>>idx)&1)
        arr[w] |= (1<<idx)
    ret = min(ret,sol(idx+1,k+1))
    x = (1<<D)-(1<<idx|1)
    #0으로 통합
    for w in range(W):
        arr[w] &= x
    ret = min(ret,sol(idx+1,k+1))
    #복구
    for w in range(W-1,-1,-1):
        arr[w] |= (temp&1)<<idx
        temp>>=1
    return ret

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    D, W, K = map(int,input().split())
    ret = K
    arr = [0]*W
    for d in range(D):
        for idx,x in enumerate(list(map(int,input().split()))):
            arr[idx]<<=1
            arr[idx] = arr[idx]|x
    ans = 0
    if not check():
        ans = sol(0,0)
    print("#"+str(test_case),ans)