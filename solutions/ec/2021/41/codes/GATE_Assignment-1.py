import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
def z(u):
  sum=0
  for k in range(-int(1e4),int(1e4)):
    if ((-k+2)>=0):
      u1=1
    else:
      u1=0
    if ((-u+k+1)>=0):
      u2=1
    else:
      u2=0
    sum=sum+2**(u+1)*u1*u2
  return sum

n=np.linspace(-8, 8, num=17)
#plots
z_n=[]
for i in n:
  z_n.append(z(i))

plt.stem(n,z_n,use_line_collection=True)
plt.title('z[n]')
plt.xlabel('$n$')
plt.ylabel('$z(n)$')
plt.grid()# minor