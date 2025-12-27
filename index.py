import numpy as np

arr = np.array([1,2,3,4,5])

copy = arr.copy()

view = arr.view()

print(arr)

copy[0] = 123
print(copy)

arr[1] =12344

print(view)

print(arr)

emp = np.empty(3)

print(emp)

