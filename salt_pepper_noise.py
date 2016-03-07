'''
Name of Programmer-Anish Hemmady
Salt and pepper noise
'''
import numpy as np
import random
import cv2
#salt and pepper noise
#it was fun programming
class add_noise:
	def __init__(self,img,amount):
		self.amnt=amount
		self.actul_amnt=1-amount
		self.img=img
	def addng_noise(self):
		finl_img = np.zeros(self.img.shape,np.uint8)
		#print self.actul_amnt
		#print finl_img.shape
		for i in range(self.img.shape[0]):
			for j in range(self.img.shape[1]):
				self.randm_val = random.random()
				if self.randm_val < self.amnt:
					finl_img[i,j] = 0
				elif self.randm_val > self.actul_amnt:
					finl_img[i,j] = 255
				else:
					finl_img[i,j] = self.img[i,j]
		return finl_img

def main():
	inp_img= cv2.imread('building.pnm',0) # grayscale image
	ob=add_noise(inp_img,0.01)
	noisy_img = ob.addng_noise()
	cv2.imwrite('noisy.png', noisy_img)

if __name__=='__main__':
	main()