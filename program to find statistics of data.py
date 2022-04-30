import math
import numpy as np

f=[4,3,2,1];
x=[140,60,100,10]

prod=np.multiply(f,x)

quot=[]
print('fx is:',prod)
for i in prod:
    quot.append(i/350)
print('mean:',quot)
xx=[]
for z,y in zip(x,quot):
    xx.append(z-y)
print('x-x:',xx)

yy=[]
for c in xx:
   yy.append(math.pow(c,2 ))
print('(x-x)^2:',yy)

aa=[]
for b,n in zip(f,yy):
    aa.append(b*n)
print('f(x-x)^2:',aa)

variant=[]

for m in aa:
    variant.append(m/350)
print('variant:',variant)
sd=[]
for j in variant:
    sd.append(math.sqrt(j))
print('sd:',sd)