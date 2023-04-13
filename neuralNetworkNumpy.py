import numpy as np
np.random.seed(0)
N,D =3,4

x = np.random.randn(N,D)
y = np.random.randn(N,D)
z = np.random.randn(N,D)

a = x*y
b = a+z
c= np.sum(b)

print("c: "+c)

grad_c = 1
grad_b = grad_c*np.ones((N,D))
grad_a = grad_b.copy()
grad_z = grad_b.copy()
grad_x = grad_a*y
grad_y = grad_a*x

print(grad_x)
print(grad_y)
print(grad_z)