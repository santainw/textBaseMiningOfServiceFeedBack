import numpy as np

#Example array
a = np.array([1,1,0])
print(".array([1,1,0]) = ",a)
print("-----------------------------------------------------------")
#Example argMax
a = np.array([[5,7,2,14],[4,5,5,11]])
print("array : ",a)
# a = np.arange(8).reshape(2, 4)
# print(a)
max = np.argmax(a)
print("Argmax = ",max)
print("-----------------------------------------------------------")


#Example max
print("array : ",a)
max = np.max(a)
print("max : ",max)
print("-----------------------------------------------------------")
x = np.array([[1,2,3],[2,2,2]])
print("array x : ",x)
print("shape of x ",x.shape)
x = np.expand_dims(x, axis=0)
# x = np.expand_dims(x, axis=0)
print("before expand_dims : ", x)
print("shape of x ",x.shape)



