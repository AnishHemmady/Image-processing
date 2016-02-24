'''
Programmer Name-Anish Hemmady
Topic-Camera Calibration 
Programming Language-Python 2.7 and core numpy libraries
'''
import numpy as np
from numpy.linalg import inv
import math
img_coords=np.array([[794,331],[456,845],[844,799],[1036,335],[1402,325],[1398,852]])
wrld_coords=np.array([[6,0,0],[18,0,14],[6,0,14],[0,4,0],[0,16,0],[0,16,14]])
#img_coords=np.array([[456,845],[514,324],[844,398],[1035,333],[1402,398],[1030,804]])
#wrld_coords=np.array([[18,0,14],[16,0,0],[4,0,2],[0,4,0],[18,0,2],[0,4,14]])
#img_coords=np.array([[458,840],[514,320],[842,332],[1080,398],[1402,324],[1034,800],[844,799],[1036,335],[1402,325],[1398,852],[514,324],[844,398]])
#wrld_coords=np.array([[18,0,14],[16,0,0],[4,0,0],[0,6,2],[0,18,0],[0,4,14],[6,0,14],[0,4,0],[0,16,0],[0,16,14],[16,0,0],[4,0,2]])
img_coords_x=[]
img_coords_y=[]
#separating out axis
img_coords_x=[i[0]for i in img_coords]
img_coords_y=[i[1]for i in img_coords]
wrld_coords_x=[]
wrld_coords_y=[]
wrld_coords_x=[i[0]for i in wrld_coords]
wrld_coords_y=[i[1]for i in wrld_coords]
wrld_coords_z=[i[2]for i in wrld_coords]
np_wrld_x=np.array(wrld_coords_x,dtype=np.float32)
np_wrld_y=np.array(wrld_coords_y,dtype=np.float32)
np_wrld_z=np.array(wrld_coords_z,dtype=np.float32)
np_img_x=np.array(img_coords_x,dtype=np.float32)
np_img_y=np.array(img_coords_y,dtype=np.float32)
B_matrix=[]
for i in range(len(np_img_x)):
	add_row_x_coord=[np_wrld_x[i],np_wrld_y[i],np_wrld_z[i],1.0,0.0,0.0,0.0,0.0,(-1.0)*np_img_x[i]*np_wrld_x[i],(-1.0)*np_img_x[i]*np_wrld_y[i],(-1.0)*np_img_x[i]*np_wrld_z[i]]
	B_matrix.append(add_row_x_coord)
	add_row_y_coord=[0.0,0.0,0.0,0.0,np_wrld_x[i],np_wrld_y[i],np_wrld_z[i],1.0,(-1.0)*np_img_y[i]*np_wrld_x[i],(-1.0)*np_img_y[i]*np_wrld_y[i],(-1.0)*np_img_y[i]*np_wrld_z[i]]
	B_matrix.append(add_row_y_coord)
#print B_matrix
B_matrix=np.array(B_matrix,dtype=np.float32)
col_vector=np.array(img_coords,dtype=np.float32)
length=2*len(np_img_x)
column_vector=np.reshape(col_vector,(length,1))
#calculate pseudo inverse of matrix B since we require pseudo inverse-->[[inverse of(B(trnspose)*B)]*B transpose]
#P_inv= np.linalg.pinv(B_matrix)
B_mat_trnsp=np.transpose(B_matrix)
sqree_mat=np.transpose(B_matrix).dot(B_matrix)
inv_sqree=inv(sqree_mat)
P_inv=inv_sqree.dot(B_mat_trnsp)
#print P_inv
#Below we obtain final B matrix but not a34 since its 1 we assumed,we obtain final matrix as normalized matrix below
finl_B_matrix=P_inv.dot(column_vector)
res2=finl_B_matrix.flatten()
res3=res2.tolist()
res3.append(1.0)
#print res3
num_arry=np.array(res3).reshape(3,4)
print num_arry
vals=num_arry[2,:-1]
total=0
for i in range(len(vals)):
	valu=vals[i]
	value=valu**2
	total=total+value
ans=math.sqrt(total)
#print ans
num_arry1=[]
#numpy_arry=num_arry.tolist()
for i in range(len(num_arry)):
	num_arry[i]=num_arry[i]/ans
	#print num_arry[i]
	num_arry1.append(num_arry[i])
normalized_matrix=np.array(num_arry1).reshape(3,4)
print "----final B matrix after finding a34 and normalization----"
print normalized_matrix
frst_row=normalized_matrix[0,:-1]#frst row 3 elements
third_row=normalized_matrix[2,:-1]#3rd row 3 elements 
second_row=normalized_matrix[1,:-1]#2nd row 3 elements
rotn_mat=normalized_matrix[:,:-1]#take frst 3 rows and 3 cols for generation of rotation matrix further down.
#print frst_row
#print third_row
first_row_store=frst_row
frst_row=np.transpose(frst_row)
uo=frst_row.dot(third_row)
vo=second_row.dot(third_row)
print "uo-->",uo
print "vo-->",vo
alpha_calc=frst_row.dot(first_row_store)
uo_sqr=uo**2
temp=alpha_calc-uo_sqr
alpha=math.sqrt(temp)
print "alpha-->",alpha
ans12=np.transpose(second_row)
Beta_calc=ans12.dot(second_row)
vo_sqr=vo**2
temp1=Beta_calc-vo_sqr
Beta=math.sqrt(temp1)
print "Beta-->",Beta
intrnsc_mat=[]
intrnsc_mat.append(alpha)
intrnsc_mat.extend((0,uo,0,Beta,vo,0,0,1))
intrnsc_mat_numpy=np.array(intrnsc_mat).reshape(3,3)
print "---intrinsic parameter matrix----"
print intrnsc_mat_numpy
intrnsc_mat_numpy_inv=inv(intrnsc_mat_numpy)
#below is rotation matrix 
#calculate extrinsics from intrinsic matrix using its inverse
print"---extrinsic parameters matrix for rotation----"
print intrnsc_mat_numpy_inv.dot(rotn_mat)
#store 3rd column of normalized matrix final B matrix i mean for generating translation matrix
ans4=normalized_matrix[:,2]
#translation matrix below
#calculate extrinsics from intrinsic matrix using its inverse
print"---extrinsic parameters matrix for translation----"
print intrnsc_mat_numpy_inv.dot(ans4)

print"----You can retain image coordinates for checking purposes using  final B matrix which is normalized matrix----"
#place world coordinates here
vk=np.array([0,12,2,1]).reshape(4,1)
checkng_matrix=normalized_matrix.dot(vk)
#print checkng_matrix

checking_mat=checkng_matrix.flatten()
for k in range(len(checking_mat)):
	checking_mat[k]=checking_mat[k]/checking_mat[2]
checking_mat=checking_mat[:-1]
x_y_values=np.array(checking_mat)
print x_y_values



