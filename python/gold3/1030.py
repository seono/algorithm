import sys


def sol(s, N, K, R1, R2, C1, C2):
    l = N**s
    plane = [[0 for _ in range(C2-C1+1)] for _ in range(R2-R1+1)]
    j = s
    while j>0:
        st = int((N-K)/2)*(N**(s-j))
        mod = N**(s-j+1)
        ed = mod-st
        for h in range(R1,R2+1):
            y = h % mod
            if y>=st and y<ed:
                for w in range(C1, C2+1):
                    x = w % mod
                    if x>=st and x<ed:
                        plane[h-R1][w-C1] = 1
        j-=1
    for i in range(R2-R1+1):
        for j in range(C2-C1+1):
            print(plane[i][j], end='')
        print()
    return

if __name__ == "__main__":
    s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split(' '))
    sol(s, N, K, R1, R2, C1, C2)
