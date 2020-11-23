import sys
input = sys.stdin.readline

#수열에 안 맞는수 중 가장 먼놈
def sol(n_list):
    n_list = [[x,i] for i,x in enumerate(n_list)]
    result = sorted(n_list, key=lambda x: x[0])
    r = 0
    for idx, n in enumerate(result):
        temp = n[1]-idx
        if temp>r:
            r=temp
    return r+1
        



if __name__ == "__main__":
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(int(input()))
    print(sol(num_list))
