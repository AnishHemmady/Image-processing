'''
Name of Programmer-Anish Hemmady
1-D Gaussian filter
'''
import math
import numpy as np
from math import exp,pi
import cv2
import time
import timeit
#start_time = timeit.default_timer()

def gaussian_kernel(size,sigma):
	if size%2==0:
		range_val=range(-int(size/2),int(size/2))
	else:
		range_val=range(-int(size/2),int(size/2)+1)
	return[1/(sigma*math.sqrt(2*pi))*(exp(-float(i)**2/(2*sigma**2)))for i in range_val]
	
arry=gaussian_kernel(9,1.5)
arry1=np.array(arry)
print arry1
img=cv2.imread('noisy.png',0)
img2=np.zeros((img.shape[0],img.shape[1]))
#1d
#do rowwise first
print img.shape
for i in range(img.shape[0]):
	for j in range(img.shape[1]-len(arry1)):
		sum=0
		
		for k in range(len(arry1)):
			#print i,j+k
			#time.sleep(2)
			sum+=img[i,j+k]*arry1[k]

		img[i,j]=sum
#get transpose of matrix to do column wise
img=np.transpose(img)
for i in range(img.shape[0]):
	for j in range(img.shape[1]-len(arry1)):
		sum=0
		for k in range(len(arry1)):
			#print i,j
			#time.sleep(2)
			sum+=img[i,j+k]*arry1[k]
		img[i,j]=sum
img=np.transpose(img)
#you can see below time elapsed time taken by this code by uncommenting below comments and above start time comment
#elapsed = timeit.default_timer() - start_time
#print elapsed
cv2.imwrite('1d4.png',img)
