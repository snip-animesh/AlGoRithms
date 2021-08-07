from collections import Counter
N=int(input())
lst=[int(x) for x in input().split()]
cyclick_lst=[]
for j in range(1,N+1):
    cyclick_lst.append((lst[j-1]-j+N)%N)
d=Counter(cyclick_lst)

while True:
    n=int(input('koto number RCS er jonne cost chao ? -'))
    x=d.get(n%N,0)
    print(N-x)
