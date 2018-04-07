#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import itertools
m=3
x=2
y=7
p=3
q=100
all_numbers=[i for i in range(x,y+1)]
print("All possible combinations are:")
for i in itertools.combinations(all_numbers,m):
    if p<=sum(i)<=q:
        i=list(i)
        # i.insert(0,x)
        # i.append(y)
        print(i)