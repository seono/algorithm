import sys
input = sys.stdin.readline
# 4231
# 4000 (1+2+3)*1000 + 4 * 232
# 10 -> 10 0
# 28 -> 0-20 20-28
# 4281 -> 0-3999 4000-4199 4200-4279 4280-4281
# (1+2+3) * 1000 + 4*4995
def cnt(num):
    if num<1:
        return 0
    i = 1
    result = 0
    while int(num/i)>9:
        i*=10
    for x in range(int(num/i)):
        result+=x
    result*=i
    n = int(num/i)
    result+=nine(i)*n
    result+=n*(num%i+1)
    return result+cnt(num%i)

def nine(num):
    i = 1
    x = num-1
    result = 0
    while int(x/i)>0:
        result = result*10 + 45*i
        i*=10
    return result

if __name__ == "__main__":
    L, U = map(int,input().split(' '))
    print(cnt(U) - cnt(L-1))