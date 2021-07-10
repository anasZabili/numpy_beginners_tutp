import numpy as np

a = np.array([1, 2, 3])

# je declare un tableau en specifiant la taille des int du tableau
matrix = np.array([[1,2, 3], [1,2, 3]], dtype=np.int16)
print(matrix)

# How to get the dimension of a numpy array

print(matrix.ndim)

# que number of row, column of a numpy array
print(matrix.shape)

# get the type of the data
print(matrix.dtype)

# Get the size of an element of the array
print(matrix.itemsize)

# get the the size of the array (in bytes)
print(matrix.itemsize * matrix.size)

# Accessing data

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [4, 7, 6, 7, 1, 4, 56, 9]])
print(array1)

# Get a specific element [row, column]

print(array1[0, 2])

# Get Row
print(array1[0, :])

#Get Column
print(array1[: , 3])

# Get subset [startIndex:endIndex:step]
print(array1[0, 1:-6:2])

# mutate a value

array1[1, 3] = 999
print(array1[1, :])

# mutate line
array2 = np.array([[1, 2, 3], [4, 5, 6]])
array2[0, :] = 3;
print(array2)
print()

# mutate column
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array3[:, 1] = 55
print(array3)

# Acces element of 3d array

array3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Array 3d \n", array3d[0, 1, 1])


# Initializing different types of arrays

# Initializing with zero
arrayZero2d = np.zeros((2,3))
print(arrayZero2d)

arrayZero3d = np.zeros((3, 4, 2))
print("\n", arrayZero3d)

#initializing with one
arrayOne3d = np.ones((3, 3, 3), dtype="int16")
print("\n", arrayOne3d)

#initializing with x
arrayX3d = np.full((2,2,2), 4, dtype="int16")
print("\n", arrayX3d)

#initializing with random float numbers (pretty usefull)
arrayRandom3d = np.random.rand(2, 2, 2)
print("\n", arrayRandom3d)

#initializing with random int number

arrayRandomInt3d = np.random.randint(low=10, size=(3,3))
print("\n", arrayRandomInt3d)

#repeat an array
arrayToRepeat = np.array([[1, 2, 3]])
arrayRepeated = np.repeat(arrayToRepeat, 3, axis=0)
print("\n", arrayRepeated)

# exercice 31:40

exerciceMatrix = np.ones((5,5), dtype="int16")
exerciceMatrix[1:-1, 1:-1] = np.zeros((3, 3))
exerciceMatrix[2, 2] = 9
print("\n",exerciceMatrix)

