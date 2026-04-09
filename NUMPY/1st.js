//Use jupyter 

import numpy as np

a = np.array((1,2,3,4,5))
print(a)


print(a.dtype,a.shape)


b = np.array((1.0,2.0,3.0,4.0,5.0))
print(b.dtype,b.shape,b.ndim)


d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d,d.shape,d.ndim) 
print(d[1][1])


a = np.array((1,2,3,4,5))
print(a[-1])
print(a[1:3])
print(a[::2])
print(a[a>2])


print(d[1:,:2])
print(d[1:2,1:3])


a = np.array((1,2,3,4,5))
b = np.array((6,7,8,9,10))
print(a+b)
print(a*b)
print(a**b)
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))
print(np.log2(a))
print(np.pow(a,2))


score = np.array((45,60,75,95,76,59))
print(np.where(score>60,"pass","fail"))



temp = np.array((38,22,15,41,30))
print(np.where(temp>37,'fever',np.where(temp<=20,'cold','normal')))



x = np.array((-3,-1,0,2,5))
print(np.where(x>0,-x,np.where(x==0,0,x**2)))
