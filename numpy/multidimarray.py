import numpy as np

array = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["U", "W", "X"], ["Y", "Z", " "]],
    ]
)

# print(array.ndim)
# print(array.shape)
# print(array[0, 0, 0])

word = (
    array[2, 0, 1]
    + array[0, 1, 1]
    + array[2, 2, 2]
    + array[0, 0, 0]
    + array[1, 1, 0]
    + array[1, 1, 2]
    + array[2, 2, 2]
    + array[1, 0, 2]
    + array[2, 0, 2]
    + array[1, 1, 1]
    + array[0, 0, 0]
)


print(word)
