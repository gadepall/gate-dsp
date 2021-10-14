import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from sklearn import metrics

N = 500
x = np.linspace(-5,5, N)

def sinc(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] == 0:
            y[i] = 1
        else:
            y[i] = np.sin(np.pi*t[i])/(np.pi*t[i])
    return y

def rect(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y

#Computing the first signal
y_1 = sinc(x)
#Computing the fourier transform
y_fourier_1 = [10*np.mean(y_1 * np.exp(1j * 2 * np.pi * f * x)) for f in x]

#Computing the second signal
y_2 = sinc(2*x)
#Computing the fourier transform
y_fourier_2 = [10*np.mean(y_2 * np.exp(1j * 2 * np.pi * f * x)) for f in x]


plt.plot(x,y_1)
plt.xlabel('$t$')
plt.ylabel('$sinc(t)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier_1), label='Simulation',color='b')
plt.plot(x,rect(x), label='Theoretical',color='r')
plt.xlabel('$f$')
plt.ylabel('$rect(f)$')
plt.grid()
plt.legend()
plt.show()

plt.plot(x,y_2)
plt.xlabel('$t$')
plt.ylabel('$sinc(2t)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier_2), label='Simulation',color='b')
plt.plot(x,0.5*rect(x/2), label='Theoretical',color='r')
plt.xlabel('$f$')
plt.ylabel('$1/2*rect(f/2)$')
plt.grid()
plt.legend()
plt.show()

print('Energy of signal f(t) : ',metrics.auc(x,np.real(y_fourier_1)**2))
print('Energy of signal f(2t) : Simulations ',metrics.auc(x,np.real(y_fourier_2)**2),'Theoretical :',metrics.auc(x,np.real(y_fourier_1)**2/2))