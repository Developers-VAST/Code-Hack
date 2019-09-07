# Author : jijinkh
n = int(input())
x = [z for z in input().split()][:n]
stri = input()


def exists(a, b):
    pos = 0
    for ch in a:
        if pos < len(b) and ch == b[pos]:
            pos += 1
    return pos == len(b)


res = ""
for i in x:
    if exists(stri, i):
        if(len(res) < len(i)):
            res = i
print(res)
