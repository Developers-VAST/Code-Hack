# Author : cirilplackal

n = int(input("Enter the range of elements "))
a = []
for num in range(0, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            a.append(num)
b = []
sum = 0
for i in a:
    sum += i
    b.append(sum)
count = 0
for i in range(len(a)):
    for j in range(1, len(b)):
        if(a[i] == b[j]):
            count += 1
print(count)
