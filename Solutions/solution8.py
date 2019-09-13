# Author : cirilplackal
n=int(input())
l=input().split()
l=list(map(int,l))
max=0
element=0
s=set(l)
for i in s:
    count=l.count(i)
    if count>max:
        max=count
        element=i
print(element)
