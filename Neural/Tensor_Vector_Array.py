# 1D Array, Vector shape is (4,) 4 elements, 1 dimension
l = [1, 5, 7, 2]

# 2D Array, Matrix, shape is (2, 4), 2 lists, 4 elements, 2 dimensions
lol = [[1, 5, 6, 2], [3, 2, 1, 3]]

# 3D Array, shape is (3, 2, 4), 3 lists of lists, 2 lists per list, 4 elements per list, 3 dimensions
lolol = [
    [[1, 5, 6, 2], [3, 2, 1, 3]],
    [[5, 2, 1, 2], [6, 4, 8, 4]],
    [[2, 8, 5, 3], [1, 1, 9, 4]]
]

# This list cannot be an array due to not being homologous
this_list = [[4, 2, 3], [5, 1]]

a = [1, 2, 3]
b = [2, 3, 4]

dot_product1 = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

print(dot_product1) # 20

dot_product2=0
for i, j in zip(a, b):
    dot_product2 +=  i*j 

print(dot_product2)
