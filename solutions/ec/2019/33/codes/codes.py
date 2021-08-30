from sympy import *

var('s')
d = Matrix([[0]])
B = Matrix([[0],[0],[1]])
I = eye(3) 

A_optionA = Matrix([[0,1,0],[0,0,1],[-1,-2,-3]])
A_optionB = Matrix([[0,1,0],[0,0,1],[-3,-2,-1]])
A_optionC = Matrix([[0,1,0],[0,0,1],[-1,-2,-3]])
A_optionD = Matrix([[0,1,0],[0,0,1],[-3,-2,-1]])

C_optionA = Matrix([[1,0,0]])
C_optionB = Matrix([[1,0,0]])
C_optionC = Matrix([[0,0,1]])
C_optionD = Matrix([[0,0,1]])

H_optionA = C_optionA*(s*I-A_optionA).inv()*B + d
H_optionB = C_optionB*(s*I-A_optionB).inv()*B + d
H_optionC = C_optionC*(s*I-A_optionC).inv()*B + d
H_optionD = C_optionD*(s*I-A_optionD).inv()*B + d

print("H_optionA =", H_optionA[0,0])
print("H_optionB =", H_optionB[0,0])
print("H_optionC =", H_optionC[0,0])
print("H_optionD =", H_optionD[0,0])
