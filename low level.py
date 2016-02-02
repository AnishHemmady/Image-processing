import numpy as np
from PIL import Image
filey=open("fish.pnm","rb")

#print lst
	
data=filey.read()
#print data
data1=data.split()
#print data1
#print(len(data1))
#print len(data1[10])
summz=0
dim_list=[]
img_type=[]
headr_dat=[]
#print data1[:9]
for i in range(0,10):
	print len(data1[i])
	if data1[i]=='P6' or data1[i]=='P5':
		img_type.append(data1[i])
		
	if data1[i]>='0' and data1[i]<'460':
		dim_list.append(data1[i])
		
	summz=summz+len(data1[i])+1
f2=open("build.pnm","wb")
type=img_type[0]
wid=dim_list[0]
ht=dim_list[1]
pnm_header=type+'\n'+"#"+' '+"Written"+' '+"by"+' '+"ImageJ"+' '+"PNM"+' '+"Writer"+"\n"+str(wid)+' '+str(ht)+"\n"+str(255)+"\n"
f2.write(pnm_header)
filey.seek(summz)
dataa=filey.read()
f2.write(dataa)


print summz
print dim_list
width=int(dim_list[0])
height=int(dim_list[1])
print width,height
print img_type
if img_type[0]=="P5":
	datta=filey.seek(50) #for building
	dat1=filey.read()
	listy=[]
	for i in dat1:
		a=ord(i)
		listy.append(a)
	print listy
	print len(listy)
	arry=np.array(listy)
	arry1=np.uint8(arry)
	#print arry1
	res=np.reshape(arry1,(height,width))
	print arry1.dtype
	imgi=Image.fromarray(res)
	imgi.save('god1245.png')
if img_type[0]=="P6":
	datta=filey.seek(15) #for motorcycle and seek(46) for fish
	dat1=filey.read()
	listy=[]
	for i in dat1:
		a=ord(i)
		listy.append(a)
	#print listy
	listy1=[]
	print len(listy)
	for i in listy:
		a=int(i)
		b=a%2**8
		listy1.append(b)
		
	arry=np.array(listy1)
	print arry.dtype
	#arry1=np.uint8(arry)
	#print arry1
	res=np.reshape(arry1,(height,width,3))
	print arry1.dtype
	imgi=Image.fromarray(res)
	imgi.save('god12458.png')

