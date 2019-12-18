#code to append one array into  another arrary
import numpy as np
a=input('enter the first array:')
b=input('enter the second  array:')
for i in range(0,len(b)):
	a.append(b[i])
print a

