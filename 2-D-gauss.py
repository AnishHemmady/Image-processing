'''
Name of Programmer-Anish Hemmady
2-D Gaussian Filter
'''
import math
import numpy as np
from math import exp,pi
import cv2
import time
import timeit
#start_time = timeit.default_timer()
def gaussn_kernl(size,sig):
	shape=(size,size)
	sigma=sig
	m,n = [(x-1.)/2. for x in shape]
	y,x = np.mgrid[-m:m+1,-n:n+1]
	q = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
	q[ q < np.finfo(q.dtype).eps*q.max() ] = 0
	sum = q.sum()
	if sum != 0:
		q/= sum
	return q

ans=gaussn_kernl(3,1.5)
print ans
#print ans.flatten()

import time
img=cv2.imread('sp_noise5.png',0)
print img.shape

for j in range(1,img.shape[0]-1):
	for i in range(1,img.shape[1]-1):
		sum=0
		for y in range(len(ans)):
			k1=ans[y]
			#convolution part
			for x in range(len(k1)):
				sum+=img[y+j-1,x+i-1]*ans[[y],[x]]

		img[j,i]=sum
#elapsed = timeit.default_timer() - start_time
#print elapsed				
cv2.imwrite('img26.png',img)


		

		



