import numpy as np

# returns the permutation matrix
# not really required
def P(N):
    p = [[0 for x in range(N)] for y in range(N)]

    for i in range(N//2):
        p[i][2*i]=1
    for i in range(N//2,N):
        p[i][2*(i-N//2)+1]=1
    return np.array(p)

# return the D matrix
def D(N):
    d = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        d[i][i]=np.exp(-1j*i*np.pi/N)
    return np.array(d)

# return the DFT matrix
def F(N):
    n = np.arange(N)
    f = np.exp(-2j*np.pi*n.reshape((N,1))*n/N)
    return f

# this is slow
# fft
# def fft(x):
#     n=len(x)
#     if n==2:
#         return np.matmul(F(2),x)
#     else :
#         # this is still slow, the time complexity will
#         # be larger because we are directly
#         # multiplying with a matrix
#         # without using its properties
#         per=np.matmul(P(n),x)
#         xe=per[:n//2]
#         xo=per[n//2:]
#         Xe=fft(xe)
#         Xo=fft(xo)
#         DXo = np.matmul(D(n//2),Xo)
#         return np.append(Xe.T+DXo.T,Xe.T-DXo.T).T

def fft(x,N=None):
    if N is None:
        n=len(x)
        x=np.append(x,np.zeros(int(pow(2,np.ceil(np.log2(n)))-n)))
        n=len(x)
    else:
        if np.ceil(np.log2(N))-np.log2(N)<1e-6 and N> len(x):
            x=np.append(x,np.zeros(N-len(x)))
            n=len(x)
        else:
            raise ValueError("N should be greater than length of sequence and should be an integral power of 2")

    if n==2:
        # stopping step, constant time
        return np.matmul(F(2),x)
    else :
        # takes O(n) time
        xe=np.array([x[i] for i in range(0,n,2)])
        xo=np.array([x[i+1] for i in range(0,n,2)])       
        
        # if fft(x) takes t(n) time
        # then using the following steps, we establish
        # t(n)=2t(n/2)+O(n)

        # Using master's theorem
        # T(n)=aT(n/b)+f(n)
        # if f(n)=O(n^{log_b{a}})
        # then T(n)=O(n^{log_b{a}}*log(n))
        # here a=2,b=2,
        # \therefore T(n) is O(n log n)
        Xe=fft(xe)
        Xo=fft(xo)
        # DXo = np.matmul(D(n//2),Xo)
        DXo = np.array([np.exp(-2j*i*np.pi/n)*Xo[i] for i in range(n//2)])
        return np.append(Xe.T+DXo.T,Xe.T-DXo.T).T

# Testing for given input
# print(fft(np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])))
