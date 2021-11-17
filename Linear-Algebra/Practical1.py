# Complex Numbers [Direct Declaraction]
a = 2+4j
b = 3-2j

# Printing Complex Numbers
print(a, '\n', b)
print()

# Using 'Complex' function
# '.imag' and '.real' works with direct declaration also.
u = complex(3, 5.3)
print("u =", u)
print("Real Part :", u.real)
print("Imaginary Part", u.imag)

print()
v = complex(5, 3)
print("v =", v)
print("Real Part :", v.real)
print("Imaginary Part", v.imag)
print()

# Arithmetic Operations on Complex Numbers
print("Addition(u+v) :", u+v)
print("Subtraction(u-v) :", u-v)
print("Multiplication(u*v) :", u*v)
print("Division(u/v) :", u/v)
