from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
# input signal
x= [1,0,2,3]
# fast fourier transform
X=fft(x)
plt.title("Magnitude of $X(k)$")
plt.xlabel("$k$")
plt.ylabel("$|X(k)|$")
plt.stem(np.abs(X))
plt.show()

plt.title("Phase of $X(k)$")
plt.xlabel("$k$")
plt.ylabel("$∠X(k)$")
plt.stem(np.angle(X))
plt.show()

print(X)