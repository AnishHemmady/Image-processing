'''
Name of Programmer-Anish Hemmady
Histogram Equalization
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2

img=cv2.imread("ct_scan.pnm",0)
width,height=img.shape
print width
print height
hist,bins=np.histogram(img,256,[0,256])
listyy=hist.tolist()
cdf=hist.cumsum()
plt.hist([img],256,[0,256])
#activate plt.show() to see histogram
#plt.show()
#cdf-cumulative distribution function
#print cdf
maxm=cdf.max()
#print maxm
minm=cdf.min()
#print minm
listy12=[]
for k in range(len(cdf)):
	val=cdf[k]
	if val!=0:
		val1=(np.cumsum(val)-minm)*255
		val2=(width*height)-minm
		val3=(val1/val2)
		val4=round(val3,2)
		listy12.append(val4)
	else:
		listy12.append(val)
	
	
#print listy12
listy12=np.array(listy12)
img2=listy12[img]

'''
#Activate this part of code by eliminating 3 quotes to get output with using histogram equalize library
#all other part implemented without using library,this code is just to cross check
img = cv2.imread('ct_scan.pnm',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res12.png',res)
'''
cv2.imwrite('histy_eqz.png',img2)

#plt.hist([img2],256,[0,256])
#plt.show()