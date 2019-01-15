import numpy as np

arr = np.random.random_integers(0,100,(5,4))

print(arr)

for i in range(0,len(arr)):
	for j in range(0,len(arr[0])):
		if(arr[i][j]>50):
			arr[i][j] = 100

print(arr)			
