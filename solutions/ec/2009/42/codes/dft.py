import numpy as np

# generates the dft matrix
def dftMatrix(N):
    n = np.arange(N)
    W = np.exp(-2j*np.pi*n.reshape((N,1))*n/N)
    return W

# calculates dft
def dft(x):
    W=dftMatrix(len(x))
    return np.dot(W,x)

x=np.array([1,0,2,3])

print(dft(x))