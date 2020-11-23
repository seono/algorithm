import sys
input = sys.stdin.readline

def sol(n_list):
    result = [n_list[0]]
    for n in n_list[1:]:
        if n>result[-1]:
            result.append(n)
        else:
            l,r = 0, len(result)-1
            while l<r:
                mid = int((l+r)/2)
                if result[mid]>=n:
                    r = mid
                else:
                    l = mid + 1
            result[r] = n
    return len(result)
    
if __name__ == "__main__":
    N = int(input())
    n_list = list(map(int, input().split(' ')))
    print(N - sol(n_list))