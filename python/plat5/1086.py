import sys
input = sys.stdin.readline

N = int(input())


def gcd(n1,n2):
    if n1<n2:
        n1,n2=n2,n1
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1

arr = [int(input()) for _ in range(N)]
K = int(input())
dp_arr = [[-1]*((1<<N)+1) for _ in range(100)]
#나머지가 rest만큼 남았을 때 i번째 수를 뒤에 붙인 값을 다시 나눈 나머지
rest_list = [[-1] * 16 for _ in range(100)]
def dp(rest,bit):
    if bit==(1<<N)-1:
        if rest==0:return 1
        else: return 0
    if dp_arr[rest][bit]!=-1:
        return dp_arr[rest][bit]
    dp_arr[rest][bit]=0


    for i in range(N):
        if 1<<i & bit:continue
        if rest_list[rest][i]==-1:
            rest_list[rest][i] = (rest*(10**len(str(arr[i])))+arr[i])%K
        dp_arr[rest][bit]+=dp(rest_list[rest][i],bit|1<<i)
    return dp_arr[rest][bit]
total = 1
for x in range(1,N+1):
    total*=x
ans = dp(0,0)
if ans==0:
    print("0/1")
else:
    g = gcd(ans,total)
    print("{}/{}".format(ans//g,total//g))