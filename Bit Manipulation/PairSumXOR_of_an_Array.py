"""Statement:Given an array with n elements calculated following -
(A1^A2)+(A1^A3)+.....+(A1^An)+
(A2^A3)+.....+(A2^An)+
(An-1^An)"""

n=int(input())
lst=[int(x) for x in input().split()]
res=0
#সংখ্যা টা ৩২ বিট এর হলে আমরা ৩১ পর্যন্ত নিব, আর ৬৪ বিট হলে ৬৩ পর্যন্ত হবে । 
for i in range(32):
    cnt0,cnt1=0,0
    for j in lst:
        if j& (1<<i):
            cnt1+=1
        else:
            cnt0+=1
    mul=cnt1*cnt0
    res+= mul<<i
    # N=N*2^i
    #N=N<<i , both are same .
print(res)
