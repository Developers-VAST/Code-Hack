# Author : jijinkh
p_amnt = int(input())
tenure = int(input())
n1 = int(input())
l2 = []
l3 = []
sum1 = 0
sum2 = 0
for i in range(n1):
    l2 = input().split(' ')
    yrs, s = float(l2[0]), float(l2[1])
    sq = ((1+s)**(yrs*12))
    emi = (p_amnt*(s))/(1-1/sq)
    sum1 = sum1 + emi
n2 = int(input())
for i in range(n2):
    l3 = input().split(' ')
    yrs, s = float(l3[0]), float(l3[1])
    sq = ((1+s)**(yrs*12))
    emi = (p_amnt*(s))/(1-1/sq)
    sum2 = sum2 + emi
if(sum1 < sum2):
    print("Bank A")
else:
    print("Bank B")
