

from GF2 import one
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


a=[one,one,one,0,0,0,0]
b=[0,one,one,one,0,0,0]
c=[0,0,one,one,one,0,0]
d=[0,0,0,one,one,one,0]
e=[0,0,0,0,one,one,one]
f=[0,0,0,0,0,one,one]
want=[0,one,0,0,0,one,0]

#[sum(a) for a in zip(a,b)] #better way to produce an array with the result we want
for subset in powerset([a,b,c,d,e,f]):
    if(([sum(a) for a in zip(*subset)])==want):
        print(subset)
