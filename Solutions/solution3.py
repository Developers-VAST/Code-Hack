# Author : jijinkh
x = int(input())
z = input()
y = [int(n) for n in z.split(' ')]
y = list(set(y))
print(sorted(y)[-2])
