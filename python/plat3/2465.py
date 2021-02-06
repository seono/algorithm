import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
cmd = list(map(int,input().split()))
ans = []
for key in cmd[::-1]:
    ans.append(arr.pop(key))
print('\n'.join(map(str,reversed(ans))))