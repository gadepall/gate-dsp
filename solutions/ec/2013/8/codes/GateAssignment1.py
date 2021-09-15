import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3,5,100)
x=[]
h=[]
y=[]

for i in t:
  if (i>=1):
    x.append(1)
  else:
    x.append(0)

for i in t:
  if (i>=0):
    h.append(i)
  else:
    h.append(0)

for i in t:
  if (i>=1):
    y.append((i-1)*(i-1)*0.5)
  else:
    y.append(0)


plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.title('input')
plt.show()


plt.plot(t,h)
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid()
plt.title('impulse response')
plt.show()

plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title('output')
plt.show()