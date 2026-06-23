import numpy as np

# para ver la version
# print(np.__version__)

# python normal
my_list = [1, 2, 3, 4]

print("lista python normal:")
print(my_list)

my_list = my_list * 2
print("lista python normal x2:")
print(my_list)

print("")
# Usando numPy
array = np.array([1, 2, 3, 4])
print("Lista numpy:")
print(array)
print("Lista numpy x2:")
array = array * 2
print(array)
