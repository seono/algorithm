import sys
input = sys.stdin.readline

N, L = map(int,input().split(' '))

def checkPossible(line):
    st = line[0]
    i = 1
    flag = 1
    while i<N:
        num = line[i]
        i+=1
        if num==st: 
            flag+=1
            continue
        if abs(num-st)>1: return False
        if num>st:
            if flag<L: return False
            flag = 1
            st = num
            continue
        temp = L-1
        #L-1개가 같은 높이여야 한다
        while temp:
            if i>=N: return False
            if line[i]!=num: return False
            temp-=1
            i+=1
        flag = 0
        st = num
    return True



arr = [list(map(int,input().split(' '))) for i in range(N)]
ans = 0
for i in range(N):
    ans+=checkPossible(arr[i])
for i in range(N):
    ans+=checkPossible([arr[j][i] for j in range(N)])
print(ans)