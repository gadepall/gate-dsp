import numpy as np

# initialising matrices involved in state space representation
T=np.array([[0,1],[1,0]])
A=np.array([[-1,1.5],[4,0]])
B=np.array([2,1])
B.reshape(2,1)
C=np.array([1.5,0.625])
C=C.T
D=1

# calculating matrices of another state space representation
bar_A=T@A@np.linalg.inv(T)
bar_B=T@B
bar_C=C@np.linalg.inv(T)
bar_D=D

# printing all the matrices
print("A=",A,",\nB=",B,"\nC=",C,",\nD=",D)
print("bar_A=",bar_A,",\nbar_B=",bar_B,"\nbar_C=",bar_C,",\nbar_D=",bar_D)

# calculating eigen values
lambda_=np.linalg.eigvals(A)
mu_=np.linalg.eigvals(bar_A)

# printing the eigen values
print("eigen values of A:",lambda_)
print("eigen values of bar_A:",mu_)
