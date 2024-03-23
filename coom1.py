l=[1,2,3,4]
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k])

import itertools
l=[1,2,3,4]
a=itertools.permutations(l,2)
for i in a:
    print(i)
