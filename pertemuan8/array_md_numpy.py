import numpy as np

array1 = np.array([90,80,70,40,])

rata = np.mean(array1)
print(rata)

print(np.median(array1))
print(np.sum(array1))

print(sum(array1 >= rata))

array2 = np.array([60,10,60,20])
array3 = np.append(array2, 100)
print(array3)