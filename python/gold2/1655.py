import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    n = int(input())
    idx = bisect.insort(arr,n)
    print(arr[int(i/2)])