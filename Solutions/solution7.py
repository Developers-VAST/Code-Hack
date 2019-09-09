# Author : INDHU-P
n = int(input("enter the number"))
s = input()
for i in range(n, 0, -1):
    print((n-i)*" "+i*"-"+s+i*"-")
for j in range(1, n+1):
    print((n-j)*" "+j*"-"+s+j*"-")
