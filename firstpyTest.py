import numpy as np
a=np.zeros((2,3))
k=0
for i in range(2):
  for j in range(3):
    a[i,j]=k
    k+=1
print("a=",a)
b=np.zeros((2,3))
b=b+1
c=a+b
  
