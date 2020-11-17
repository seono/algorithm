import sys

def solution(l, r):
    result = 1
    if l>r-l:
        l = r-l
    temp = l
    l = 1
    while temp>0:
        result*=r
        r-=1
        temp-=1
        result/=l
        l+=1
    return int(result)

if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for t in range(testcase):
        l, r = sys.stdin.readline().split(' ')
        print(solution(int(l), int(r)))