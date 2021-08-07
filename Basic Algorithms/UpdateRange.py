n=int(input())
lst=[int(x) for x in input().split()]
update=[0]*n
for _ in range(int(input())):
    L,R,X=map(int,input().split())
    update[L-1]+=X
    update[R]-=X
cnt=0
for i in range(n):
    cnt+=update[i]
    lst[i]+=cnt
print(lst)

#L006 from CodeNcode
