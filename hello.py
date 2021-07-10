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
print("\n fill with zero 3d", arrayZero3d)

#initializing with one
arrayOne3d = np.ones((3, 3, 3), dtype="int16")
print("\n fill with one 3d ", arrayOne3d)

#initializing with x
arrayX3d = np.full((2,2,2), 4, dtype="int16")
print("\n fixed number 3d", arrayX3d)

#initializing with random float numbers (pretty usefull)
arrayRandom3d = np.random.rand(2, 2, 2)
print("\n random number int", arrayRandom3d)

#initializing with random int number

arrayRandomInt3d = np.random.randint(low=10, size=(3,3))
print("\n fill a matrix with random numbers", arrayRandomInt3d)

#repeat an array
arrayToRepeat = np.array([[1, 2, 3]])
arrayRepeated = np.repeat(arrayToRepeat, 3, axis=0)
print("\n repeated array", arrayRepeated)

# exercice 31:40

exerciceMatrix = np.ones((5,5), dtype="int16")
exerciceMatrix[1:-1, 1:-1] = np.zeros((3, 3))
exerciceMatrix[2, 2] = 9
print("\n exercice matrix",exerciceMatrix)

# copy array

a = np.array([1, 2, 3])
b = a.copy()


# Mathematics

# all the classique mathe operation works with arrays

addArray = np.array([[1, 2, 3]]) + 6
print("\n add constant to an array", addArray)

# trigo operarion

sinArray = np.array([1, 2, 3])
print("\n sinus of array", np.sin(sinArray))

# Linear algebra
# mutiplie matrix
a = np.ones((2, 3))
b = np.full((3, 2), 2)
print("\n matrix multiplication", np.matmul(a, b))

# Determinante of a matrix
c = np.identity(3)
print("\n determinant", np.linalg.det(c))

#Statistics

stats = np.array([[4, 5, 6], [7, 8, -1]])
# axis=0 coupe vertical du tableau
# axis=1 coupe horizontal du tableau
print("\n min stats", np.min(stats, axis=0))
print("\n max stats", np.max(stats, axis=1))


# Reorganizing arrays

# reshape array
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# when performing a reshape the new structure need to have the same number of elements
print("\n reshape array", before.reshape((2, 2, 2)))

# vertically stacking vectore
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print("\n merge of two array stacked vertically to create a matrix\n", np.vstack([v1, v2]))

# horizontal stack (need to have the same number of rows)
vh1 = np.zeros((2, 2))
vh2 = np.ones((2, 4))

print("\n merge of two array stacked horizontal to create a matrix\n", np.hstack([vh1, vh2]))


# Load date from file

fromFileArray = np.genfromtxt("data.txt", delimiter=",", dtype="int16")
# converte the generated array to  other types
convertedArray = fromFileArray.astype("float32")
print("\n array generated from textFile", fromFileArray)


# Boolean masking and advanced dindexing (very usefull)
# we can use this concept to apply a condition on each of our element

print("\n apply boolean mask on each element", fromFileArray > 50)


# Get only the element who passed the mask (usefull aswell )

print("\n print only the element who respect the condition", fromFileArray[fromFileArray > 50])

# Check if any of the value of the column are greater than 50

print("\n  Check if any of the value of the column are greater than 50", np.any(fromFileArray > 50, axis=0))
print("\n  Check if all of the value of the column are greater than 50", np.all(fromFileArray > 50, axis=0))

# boolean operator 