st = input()
no = int(input())
z = [n for n in st]
for i in range(0, len(z), no):
    print(''.join(z[i:i+no]))
