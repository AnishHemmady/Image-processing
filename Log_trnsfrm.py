'''
Name of Programmer-Anish Hemmady
Log transformation
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

img=cv2.imread("auto.pnm",0)
width,height=img.shape
img2=img
print width
print height
hist,bins=np.histogram(img.flatten(),256,[0,256])
listyy=hist.tolist()


img2=img
img2.astype(np.float)

c = (img2.max()) / (img2.max()**(0.5))
for i in range(0,img2.shape[0]):
    for j in range(0,img2.shape[1]):
		val=img2[i,j]
		img2[i,j]=c*math.log(1+val,2)
		
	
	
	
img2 = img2.astype(np.uint8)
#print img2

plt.imshow(img2,cmap=plt.get_cmap('gray'))
plt.xticks([])
plt.yticks([])
plt.savefig('log_out4.png')
#plt.show()
