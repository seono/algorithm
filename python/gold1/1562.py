import sys
input = sys.stdin.readline

def sol(i):
    arr = [[[-1]*((1<<11)+1) for _ in range(10)] for _ in range(100)]
    INF = int(1e9)
    N = i

    def dp(cnt, num, bit):
        if(num<0 or num>9):
            return 0
        if cnt==N:
            if bit == ((1<<10)-1):
                return 1
            else:
                return 0
        if arr[cnt][num][bit]!=-1:
            return arr[cnt][num][bit]
        arr[cnt][num][bit]=0
        if bit==0:
            for i in range(1,10):
                arr[cnt][num][bit]+=dp(cnt+1,i+1,1<<i)
                arr[cnt][num][bit]+=dp(cnt+1,i-1,1<<i)
        else:
            if cnt==N-1:
                arr[cnt][num][bit]+=dp(cnt+1,num,bit|1<<num)
            else:
                arr[cnt][num][bit]+=dp(cnt+1,num+1,bit|1<<num)
                arr[cnt][num][bit]+=dp(cnt+1,num-1,bit|1<<num)
        arr[cnt][num][bit]%=INF
        return arr[cnt][num][bit]
    return dp(0,0,0)
print(sol(int(input())))