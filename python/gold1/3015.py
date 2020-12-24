import sys
input = sys.stdin.readline

n = int(input())
st = []
ans = 0
for _ in range(n):
    i = int(input())
    while st and st[-1][0]<i:
        ans+=st.pop()[1]
    if st and st[-1][0]==i:
        cnt = st.pop()[1]
        ans+=cnt
        if st:
            ans+=1
        st.append([i,cnt+1])
    else:
        if st:
            ans+=1
        st.append([i,1])
print(ans)