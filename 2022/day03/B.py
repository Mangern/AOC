from functools import reduce
import sys
with open(sys.argv[1],"r")as f:
    l=list(map(lambda x:x.strip(),f.readlines()))
s=0
p=lambda c:ord(c)-ord("A")+27 if ord(c)<=ord("Z") else ord(c)-ord("a")+1
for a,b,c in zip(l[::3],l[1::3],l[2::3]):
    a,b,c=map(lambda n:reduce(lambda cr,x: cr|set((x,)),n,set()),(a,b,c))
    s+=p(reduce(lambda cr,x:cr.intersection(x),(b,c),a).pop())
print(s)
