import glob
#import pymorph
from matplotlib import pyplot as plt
import PIL.ImageOps
from PIL import Image
import random
import math
import numpy
import numpy as np
from scipy import ndimage
from scipy import misc
from skimage.morphology import medial_axis
import time

images  =  glob.glob("*.tif")
imagenum = 0
for image in images:
	imagenum = imagenum + 1
	print (imagenum)
	image = image[:-4]
	print (image)
	name = image
	sname = name + ".tif"
	bname = name + "t1testb.tif"
	bkname = name + "t1testbk.tif"
	bkbname = name + "t1testbkb.tif"
	bkbiname = name + "t1testbkbi.tif"
	bkbisname = name + "t1testbkbis.tif"
	finname = name + "t1testfin.tif"

	print ("starting blur")
	img = cv2.imread(sname,0)
	blur = cv2.GaussianBlur(img,(9,9),0)
	median = cv2.medianBlur(blur,9)
	cv2.imwrite(bname,median)
	img1=cv2.imread(bname,0)
	hist=cv2.calcHist([img1],[0],None,[256],[0,256])
	plt.hist(img1.ravel(),256,[0,256])
	#time.sleep(10)
	print(hist)
	listyy=list()
	#listyy.append(hist)
	print(hist.tolist())
	print(len(hist))
	for i in range(1,255):
		if hist[i]>hist[i+1] and hist[i]<hist[i-1]:
			listyy.append(hist[i].tolist())
	print(listyy)
	print(len(listyy))
	#print(listyy.tolist())
	plt.show()
	imgy1=Image.open(bname)
	pixl=imgy1.load()
	for x in range(0,imgy1.size[0]):
		for y in range(0,imgy1.size[1]):
			if pixl[x,y]<196:
				pixl[x,y]=255
			else:
				pixl[x,y]=0
	
	imgy1.save("wrkng.tif")
	