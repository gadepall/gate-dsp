import numpy as np
import math
from matplotlib import pyplot as plt

# sampling rate = 60kHz
sr = 30000
t = np.linspace(0,1,20*sr)
ts = np.linspace(0,1,sr)
T = 1/sr

# Signal x(t)
x   = np.cos(2*np.pi*10000*t)
# signal x(1+t/2)
x1 = np.cos(2*np.pi*10000*(1+(t/2)))
# signal y(t)
y = x*x1

# Signal x(t)
xs   = np.cos(2*np.pi*10000*ts)
# signal x(1+t/2)
x1s = np.cos(2*np.pi*10000*(1+(ts/2)))
# signal y(t)
ys = xs*x1s


n = 0
interpolate = 0
for n in range(len(ts)):
  interpolate = interpolate + ys[n]*np.sinc((t-n*T)/T)

#plt.plot(t[0:50],y[0:50])
plt.stem(ts[0:50],ys[0:50])
plt.plot(t[0:1000],interpolate[0:1000],color='g')
