'''
Name of programmer-Anish Hemmady
Median filter
'''
import cv2
import numpy as np
import time
def quicky_sort(res):
	if len(res)>1:
		middle_ele=len(res)/2
		small_elements=[]
		large_elements=[]
		
		for i,ele in enumerate(res):
			if i!=middle_ele:
				if ele<res[middle_ele]:
					small_elements.append(ele)
				else:
					large_elements.append(ele)
					
		quicky_sort(small_elements)
		quicky_sort(large_elements)
		res[:]=small_elements+[res[middle_ele]]+large_elements
	return res

img=cv2.imread("sp_noise1.png",0)
width,height=img.shape
#print img
#padding of image with 1 row above and below and 1 column on lhs and rhs of image matrix
npad=((1,1),(1,1))
img=np.pad(img,pad_width=npad,mode='constant', constant_values=0)
#print img
#3 by 3 window mask
window=np.zeros((3,3))
width_window=3
height_window=3
edge_x=int(width_window/2)
edge_y=int(height_window/2)
for i in range(0,width):
	for j in range(0,height):
		for k in range(0,width_window):
			for l in range(0,height_window):
				val23=img[i+k-edge_x,j+l-edge_y]
				window[[k],[l]]=val23
		wind1=window.flatten()
		wind1=wind1.tolist()
		valus=quicky_sort(wind1)
		length=len(valus)
		median_val=valus[int(length/2)]
		img[i,j]=median_val
cv2.imwrite('img1.png',img)
				


			