import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-2*np.pi-1,2*np.pi+1,1000)
y = 1/(1-(5/6)*(np.exp(-1j*omega))) +  1/(1-(6/5)*(np.exp(-1j*omega)))

amp = (y*np.conj(y))**(0.5)

plt.plot(omega,amp)
plt.ylim(0,6)
plt.grid()
plt.xlabel("w")
plt.ylabel("|H(w)|")

plt.show()
