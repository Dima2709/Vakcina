import random as rd
st = ['']
slovar = {}
s = ''
for i in range(1000):
    while str(s) in st:
        s = rd.randint(10000,99999)
        st.append(str(s))
print(st)