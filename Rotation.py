'''
Name of the Programmer-Anish Hemmady
Rotation of image by given angle
'''
import numpy as np
import cv2
import math
import time
from matplotlib import pyplot as plt
#backwards approach used
img=cv2.imread("building.png",0)
width,height=img.shape
theta=45
theta=(theta*3.14)/180
x_center=width/2
y_center=height/2
rotn_mat=[]
#generate inverse rotation matrix
rotn_mat.extend((math.cos(theta),math.sin(theta),-math.sin(theta),math.cos(theta)))
rotn_mat=np.array(rotn_mat)
rotn_mat=np.reshape(rotn_mat,(2,2))
#print rotn_mat
#you can keep new width and new height here and chnage img2 shape with new width and height
#to see changes.
#new_width=width*math.cos(theta)+height*math.sin(theta)
#new_height=height*math.cos(theta)+width*math.sin(theta)
img2=np.zeros((img.shape[0],img.shape[1]))
for i in range(img2.shape[0]):
	for j in range(img2.shape[1]):
		trns=[]
		#print i,j,x_center,y_center
		x=i-x_center
		y=j-y_center
		trns.extend((x,y))
		trns=np.array(trns)
		trns=np.reshape(trns,(2,1))
		res=rotn_mat.dot(trns)
		res=res.flatten()
		x2=res[0]
		y2=res[1]
		x2=x2+x_center
		y2=y2+y_center
		
		
		if(x2<0):
			pass
		elif(y2<0):
			pass
		elif(x2>width):
			pass
		elif(y2>height):
			pass
		else:
			#print x2,y2
			val=img[x2,y2]
			#print val
			img2[i,j]=val
			#time.sleep(2)
cv2.imwrite('imgk2.png',img2)

#uncomment below to see the magic of inbuilt library of rotation.Above see the magic of my code.
'''
import cv2
img = cv2.imread('building.pnm',0)
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('img_rotn_lib.png',dst)'''

		
		


