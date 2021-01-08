import sys
import bisect
input= sys.stdin.readline
print = sys.stdout.write
N = int(input())
end_max = N*2+1
arr = [0]*(end_max+1)
arr[end_max//2]=int(input())
cnt = 0
print("%d\n"%cnt)
ans = [0]
for _ in range(N-1):
    n = int(input())
    st,ed = 0,end_max
    mid = (st+ed)//2
    dep = 0
    while arr[mid]:
        if arr[mid]>n:
            ed = mid-1
        else:
            st = mid+1
        mid = (st+ed)//2
        dep+=1
    arr[mid]=n
    cnt+=dep
    print("%d\n"%cnt)

#N(logN) 시간 초과 실패


def sol():
    N = int(sys.stdin.readline().rstrip())
    MAX_N = 300000
    left = [0] * (MAX_N + 2)
    right = [0] * (MAX_N + 2)
    lev = [0] * (MAX_N + 2)
    data = [0] * (MAX_N + 1)
    C = 0
    result = []
    for i in range(1, N + 1):
        data[i] = int(sys.stdin.readline().rstrip())
        left[i] = i - 1
        right[i] = i + 1
    for i in range(N, -1, -1):
        right[left[data[i]]] = right[data[i]]
        left[right[data[i]]] = left[data[i]]
    lev[0] = lev[N + 1] = -1
    for i in range(1, N + 1):
        lev[data[i]] = max(lev[left[data[i]]], lev[right[data[i]]]) + 1
        C += lev[data[i]]
        result.append(str(C))
    print('\n'.join(result))


if __name__ == "__main__":
    sol()
