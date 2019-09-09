# Author : Abilash1907
def compare(s1, s2):
    m = len(s1)
    n = len(s2)
    j = 0
    i = 0
    while (i < n and j < m):
        if (s1[j] == s2[i]):
            j += 1
        i += 1
    return (j == m)


def longest(d, st):
    r = ""
    le = 0
    for i in d:
        if (le < len(i) and compare(i, st)):
            r = i
            le = len(i)
    return r
n = int(input())
l = input("dict=").split(' ')
l = {n for n in l}
s = input("str=")
print(longest(l, s))
