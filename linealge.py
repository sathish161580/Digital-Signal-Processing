#code on linear algebraic operations
import numpy as np
a=np.array(input('enter the  matrix:'))
b=np.array(input('enter the another matrix:'))
f=np.dot(a,b)
print 'Multiplication of two matrices:\n',f
z=np.linalg.eig(a)
print 'Eigen vectors of\n',a,'\n is:',z
w=np.linalg.matrix_rank(a)
print 'Rank of a matrix of\n',a,'\n is:',w
u=np.add(a,b)
print 'Addition of two matirces:\n',u
v=np.subtract(a,b)
print 'Subtraction of two matrices:\n',v
e=np.multiply(a,b)
print 'element by element multiplication of two matrices:\n',e
k=np.divide(a,b)
print 'element by element division of two matrices:\n',k
y=np.linalg.inv(a)
print 'inverse of\n',a,'\n is:',y
g=np.linalg.matrix_power(a,3)
print 'matrix power of\n',a,'\n is:',g
x=np.linalg.det(a)
print 'Determinent of\n',a,'\n is:',x
s=np.linalg.eigvals(a)
print 'Eigen values of\n',a,'\n is:',s
t=np.linalg.qr(a)
print 'qr decomposition of\n',a,'\n is:',s


