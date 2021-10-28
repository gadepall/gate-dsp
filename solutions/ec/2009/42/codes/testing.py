# Tested for 
# https://www.sathyabama.ac.in/sites/default/files/course-material/2020-10/UNIT3_1.pdf
import time
from fftFromScratch import *

import matplotlib.pyplot as plt
x=np.array([1,1,1])

plt.stem(x,label='$x[n]$')
plt.grid()
plt.legend()
plt.show()

X=fft(x.T,4)
plt.stem(np.abs(X),label='|X[k]|')
plt.grid()
plt.legend()
plt.show()

plt.stem(np.angle(X),label='∠X[k]')
plt.grid()
plt.legend()
plt.show()

def nlogn(x):
    return x*np.log2(x)


# Now, testing for randomly generated sequences
timeDict={}
series2 = [4*pow(2,i) for i in range(15)]



gibberish=[]
for i in series2:
    gibberish.append(np.random.rand(i))
for i in series2:
    StartTime = time.time()
    Fourier = fft(gibberish[round(np.log2(i/4))])
    endTime=time.time()
    timeTaken = endTime-StartTime
    timeDict[i]=timeTaken

print(timeDict.values())

plt.scatter(timeDict.keys(),timeDict.values(),color='red',label='time taken for differen N')

# building a n log n series
NLOGn=nlogn(series2)
print(timeDict.values())
# x is just array containing time taken by different DFT
x = np.array(list(timeDict.values()),dtype=float)
n = np.array(NLOGn,dtype=float)
# k is the hyper parameter
# which minimized || kn-x||^2 (l2 norm) k is a scalar.
# this is just a quadratic
# the solution is 
# (x.T n) /(n.T n)
k=np.dot(x,n)/np.dot(n,n)
print(k)
NLOGn=k*NLOGn
# plotting N log N
plt.plot(series2,NLOGn, label='$k N \log N$')
plt.xlabel("Value of $n$")
plt.ylabel("Time in seconds")
plt.grid()
plt.legend()
plt.show()

# plt.stem(t2,y,use_line_collection=True)
