import numpy as np

# array = np.array([[1,2,3,4,5],[12,23,45,67,1234]])

# result = array*2

# print(result)
# print(array.shape)
# print(array.size)
# print(array.ndim)



# print(arr>10)
# print(arr[True])

# print(arr[arr>10])
# arr[arr<0] =0

# print(arr)

# print(arr[::-1]) 

# print("Mean: ",np.mean(arr))
# print("Median: ",np.median(arr))
# print("mode: ",np.mod(arr))
# print("std dev:",np.std(arr))

# print(arr.reshape(2,3))

# print("max index :",np.argmax(arr))
# print("min index: ",np.argmin(arr))

# arr = np.array([1,2,34,56,78,-12,1])
# arr1 = np.array([1,2,34,56,78,-12,1])

# print(np.sum(arr*arr1))

# sorted_index = np.argsort(arr)
# print(sorted_index)
# print(arr[sorted_index])

# print(np.array_equal(arr,arr1))

# print(np.unique(arr))

# arr12 = np.array([10,20,30,40])

# normalized = (arr-arr.min()/(arr.max()-arr.min()))

# print(normalized)


# arr11 = np.array([1,2,np.nan,4,5])

# mean_val = np.nanmean(arr11)

# arr11[np.isnan(arr11)] =mean_val

# print(arr11)


arr = np.array([[1,2,3,4],[5,6,7,8]])

# print("Row-wise sum :",arr.sum(axis=1))

# print("column wise sum: ",arr.sum(axis=0))
# print(arr.flatten())

# print(arr.ravel())

arr1 = np.array([1,2,3])

result = arr + np.array([[10],[20]])

# print(result)

a = np.array([1,2,3,4,5,6])

b= np.array([2,3,4,5,6,7])

# print("Intersection: ",np.intersect1d(a,b))

# print("Difference: ",np.setdiff1d(a,b))

values , count = np.unique(a,return_counts=True)

print(dict(zip(values,count)))
