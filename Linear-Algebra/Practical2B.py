import numpy as np
u = np.array((3, 4, 5))
v = np.array((1, 5, 6))

print("Vector u", u)
print("Vector v", v)

a = int(input(">"))
print("Value of a :", a)

b = int(input(">"))
print("Value of b :", b)

# Adding Vectors by u*a + b*v
d = (a*u)+(b*v)

print("Addition Vector of u & v :", d)
print("Dot Product of u & v :", np.dot(u, v))
