import numpy as np
import matplotlib.pyplot as plt

a = 1.0
b = 2.0
c = 3.0
d = 4.0

abcd = np.array([a,b,c,d])

pqrs = np.matmul(abcd, np.array([[a,b,c,d],[d,a,b,c],[c,d,a,b],[b,c,d,a]]))

def DFT(x):

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    
    X = np.dot(e, x)
    
    return X
    
dft_abcd = np.round(DFT(abcd),0)

dft_pqrs = np.round(DFT(pqrs),0)

predicted_dft_pqrs = dft_abcd**2

print("[Alpha Beta Gama Delta] = ", dft_abcd)
print("[Alpha^2 Beta^2 Gama^2 Delta^2] = ", predicted_dft_pqrs)
print("DFT of [p q r s]", dft_pqrs)
