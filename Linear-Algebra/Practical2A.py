# Vectors
"""
Vectors are lists []
"""

u = [2, 4, 3]
v = [3, 1, 5]

# Random Number list
a = [9, 8, 1]
b = [3, 6, 1]


# Adding Two Vectors


def add(u, v):
    return[a[i]*u[i]+b[i]*v[i] for i in range(len(u))]


print("Addition of vectors : ", add(u, v))
print("Addition of vectors : ", add(v, u))


# Multiplication of Vectors


def dot(u, v):
    if len(u) == len(v) and len(u) != 0:
        return [u[i]*v[i] for i in range(len(u))]
    else:
        return 0


print("Multiplication of Vectors :", dot(u, v))
print("Multiplication of Vectors :", dot(v, u))
