#Author : Jijin
st = input()
st_set = set(st)
c = {}
for i in st_set:
    c[i] = st.count(i)
x = []
for i in c.values():
    x.append(i)
x = set(x)
if(len(x) == 1):
    print("Valid")
elif(len(x) == 2):
    x = list(x)
    if(abs(x[0]-x[1]) == 1):
        print("Valid")
    elif(x[0] == 1):
        print("Valid")
else:
    print("Not Valid")
