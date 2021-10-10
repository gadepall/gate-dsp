import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

num=[1]
den=[1,2]

sys = signal.TransferFunction(num, den)

time = signal.step(sys)[0]
response = 10*signal.step(sys)[1]
n = len(time)
for i in range(n):
    if(response[i]>=0.99*response[n-1]):
        print('Time at which output siganl reaches 99% of steady state value is ',time[i],'sec (approx)')
        break

plt.plot(time,response,label="Simulation")
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()