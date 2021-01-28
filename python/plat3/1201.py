import sys
input = sys.stdin.readline


def sol():
    N, M, K = map(int,input().split())
    if N-M+1<K:
        return [-1]
    else:
        if M>=K:
            arr = [n for n in range(N-M+1,N+1)]
            #남은수 N-M
            N-=M
            #증가수열 K-1개 더만들기
            K-=1
            if K==0:
                if N==0:
                    return arr
                else:
                    return [-1]
            num = N//K
            if num>M:
                return [-1]
            #길이는 num(남은 수 N / K)
            while N:
                tmp = []
                for _ in range(num):
                    tmp.append(N)
                    N-=1
                K-=1
                if K==0:
                    while N:
                        tmp.append(N)
                        N-=1
                arr.extend(tmp[::-1])
                tmp = []
            return arr
        else:
            arr = [n for n in range(K,0,-1)]
            M-=1
            #감소수열 M개 더만들기
            if M==0:
                if N==K:
                    return arr
                else:
                    return [-1]
            num = (N-K)//M
            if num>K:
                return [-1]
            i = K+1
            while i<=N:
                tmp = []
                for _ in range(num):
                    tmp.append(i)
                    i+=1
                M-=1
                if M==0:
                    while i<=N:
                        tmp.append(i)
                        i+=1
                arr.extend(tmp[::-1])
                tmp = []
            return arr
print(' '.join(map(str, sol())))
