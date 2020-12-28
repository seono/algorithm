import sys
input = sys.stdin.readline

while True:
    arr = list(map(int,input().split()))
    x = arr.pop(0)
    if x==0:
        break
    st = []
    ans = 0
    for i in range(len(arr)):
        while st and arr[i]<arr[st[-1]]:
            n = st.pop()
            width = i
            if st:
                width = i-st[-1]-1
            height = arr[n]
            ans = max(ans,width*height)
        st.append(i)
    n = len(arr)
    while st:
        i = st.pop()
        width = n
        if st:
            width = n - 1 - st[-1]
        height = arr[i]
        ans = max(ans,width*height)
    print(ans)