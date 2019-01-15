import pandas as pd

df = pd.read_table('q1dat.log')
var = 0
list1 = df.values.tolist()
for i in range(0,len(list1)):
	item = list1[i][0].split(' ')
	#print(item)
	if(item[0] == 'D'):
		var = var + int(item[1])
	if(item[0] == 'W'):
		var = var - int(item[1])
			
print(var)	


