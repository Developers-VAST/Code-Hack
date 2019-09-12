# Author : jijinkh
no = int(input())
lis = [int(n) for n in input().split(' ')][:no]
pts = 0
mx = lis[0]
for i in lis:
    if i > mx:
        pts += mx
        mx = i
    else:
        pts += i
pts += 25 * mx
pts -= lis[0]
print(pts)
