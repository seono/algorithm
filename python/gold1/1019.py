import sys
input = sys.stdin.readline()

N = int(input)
def sol():
    arr2 = [0]*10
    for i in range(1,11):
        temp = 1
        while N//temp>0:
            arr2[i%10]+=N//(temp*10)*(temp)
            if N//temp%10>i:
                arr2[i%10]+=(temp)
            elif N//temp%10==i%10:
                arr2[i%10]+=N%temp+1
                if i==10:
                    arr2[i%10]-=temp
            temp*=10
    print(' '.join(map(str,arr2)))
sol()