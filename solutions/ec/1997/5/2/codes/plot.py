import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 6, 3

N = 500
x = np.linspace(-5,5, N)

def rectFunction(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y
#Computing the rectangular function
y1 = rectFunction(x/2)
#Computing the fourier transform
y_fourier1 = [10*np.mean(y1 * np.exp(-1j * 2 * np.pi * f * 2*x)) for f in x]
#Comparing it with the theoretical result
y_theoretical1 = 2 * (np.sin((2 * np.pi *2* x))/((2 * np.pi * 2*x)))

plt.plot(x,y1)
plt.xlabel('$t$')
plt.ylabel('$x(t/2)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier1), label='Simulation',color='b')
plt.plot(x,np.real(y_theoretical1), label='Theoretical',color='r')
plt.xlim(-5,5)
plt.xlabel('$f$')
plt.ylabel('$X(f)$')
plt.grid()
plt.legend()
plt.show()


#Computing the rectangular function
y2 = rectFunction(x-2)
#Computing the fourier transform
y_fourier2 = [10*np.mean(y2 * np.exp(-1j * 2 * np.pi * f * x)) for f in x]
#Comparing it with the theoretical result
y_theoretical2 = np.exp(-1j * 2* 2 * np.pi * x) * (np.sin((2 * np.pi * x)/2)/((2 * np.pi * x)/2))

plt.plot(x,y2)
plt.xlabel('$t$')
plt.ylabel('$x(t-2)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier2), label='Simulation',color='b')
plt.plot(x,np.real(y_theoretical2), label='Theoretical',color='r')
plt.xlim(-5,5)
plt.xlabel('$f$')
plt.ylabel('$X(f)$')
plt.grid()
plt.legend()
plt.show()
#"""
fig, ax = plt.subplots(2,1)
#Plotting the signals of amplitude
ax[0].plot(x, np.absolute(y_fourier2), label="$Simulation$")
ax[0].plot(x, np.absolute(y_theoretical2), label="$Theoretical$")
ax[0].set_ylabel("$A$")
ax[0].legend(loc = "best")
ax[0].grid()
plt.xlabel("$f$")
#Plotting the phase
ax[1].plot(x, np.angle(y_fourier2), label="$Simulation$")
ax[1].plot(x, np.angle(y_theoretical2), label="$Theoretical$")
plt.xlabel("$f$")
ax[1].set_ylabel("$\phi$")
ax[1].legend(loc = "best")
ax[1].grid()
plt.show()
#"""
