import numpy as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# array[start:end:step]

# row
print("Row:")
print(array[0:4:2])
print(" ")
print(array[::-1])
print(" ")
print(array[::-2])

# columna
print("")
print("Columna:")
print(array[:, 1])
print(array[:, 0])
print("")
print(array[:, 0:3:])

# row y columna
print("")
print("row y columna:")
print(array[0:2, 0:2])
print("")
print(array[0:2, 2:])
print("")
print(array[2:, 0:2])
print("")
print(array[2:, 2:])
