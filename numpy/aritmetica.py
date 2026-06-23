import numpy as np

# Scalar arithmetic

array = np.array([1.50, 2.45, 3.87])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array**5)

# Vectorized math functions
print("")
print("Vectorized math functions")

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)

# Ejercicio 1
print("")
print("")
print("Ejercicio area de un circulo")

radio = np.array([2, 4, 5])
print(np.pi * radio**2)

# Element-wise arithmetic
print("")
print("")

array1 = np.array([5, 6, 7])
array2 = np.array([8, 9, 1])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1**array2)

# Comparison operators
print("")
print("")

scores = np.array([91, 89, 78, 99, 100, 50])
print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)
