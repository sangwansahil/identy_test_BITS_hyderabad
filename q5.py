import numpy as np

bool_arr = np.random.choice(a=[False, True], size=10)
arr = np.random.randint(100, size=10)

final = []

for i in range(0,len(arr)):
	if(bool_arr[i]==True):
		final.append(arr[i])
		
print(bool_arr)
print(arr)
print(final)		
