n=int(input(),2)
cnt=0
while n!=0:
    if n&1!=0:
        cnt+=1
    n=n>>1
print(cnt)

# Complexity O(logn) of both coz each time we are dividing a number by 2 

n=int(input(),2)
cnt=0
while n>0:
    cnt+=1
    n=n&(n-1)
print(cnt)
