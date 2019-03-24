import random
import numpy as np
from copy import  deepcopy

def live_neighbours(i,j):
	n = 0	
	for a in [i-1, i, i+1]:
		for b in [j-1, j, j+1]:
			if(a == i and b == j):
				continue	#the cell itself - ingore it
			if((a>=0 and b >= 0) and (a<len(uni) and b <len(uni[0]))):
				n += uni[a][b]
	return n 

def copy_unis(a, b):
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] == 1:
				b[i][j] = 'X'
			if a[i][j] == 0:
				b[i][j] = '.'

if __name__ == '__main__':
	x = input("give x value: ")
	y = input("give y value: ")

	


	uni = [[random.randint(0,1) for i in range(x)] for j in range(y)] 	#as universe

	uni_2 = [[0 for i in range(x)] for j in range(y)]

	print "len uni = " , len(uni)
	print "cols = " , len(uni[0])
	copy_unis(uni, uni_2);

	
	alt_uni = [[0 for i in range(x)] for j in range(y)]  #as alternate universe to keep track of changes

	print(np.matrix(uni_2))
	print("*********************************")
	alt_uni = deepcopy(uni)
	otinanai = raw_input("pata enter kai pame")
	neibs = [[0 for i in range(x)] for j in range(y)]

	while(1):
		for i in range(len(uni)):
			for j in range(len(uni[0])):
				live = live_neighbours(i, j)
				neibs[i][j] = live
				
				if(uni[i][j] == 1 and live < 2):
					alt_uni[i][j] =0
				elif(uni[i][j] == 1 and (live == 2 or live ==3)):
					alt_uni[i][j] = 1
				elif(uni[i][j] ==1 and live > 3):
					alt_uni[i][j] = 0
				elif(uni[i][j] == 0 and live == 3):
					alt_uni[i][j] =1
			
		#print(np.matrix(neibs))
		uni =deepcopy(alt_uni)
		copy_unis(uni, uni_2);
		print("******************")
		print(np.matrix(uni_2))
		raw_input("next")

	