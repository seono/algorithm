import sys

sys.stdin = open("input.txt", "r")
cnt = 0
def gcd(a,b):
    global cnt
    cnt+=1
    return gcd(b,a%b)+a//b if b else a-1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    cnt = 0
    print("#"+str(test_case),gcd(a,b)-1)
    print(cnt)