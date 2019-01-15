import numpy as np

arr = np.random.randint(100, size=10)


for i in range(1,len(arr),2):
	arr[i] = -10
	
print(arr)		
