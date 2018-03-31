import json

def read(filename):
	f=open(filename+'.txt','r')
	return json.load(f)
	f.close()

def multiple(matrixA,matrixB):
	result=[[0]*10 for i in range(10)]
	for i in range(len(matrixA)):
		# iterate through columns of Y
		for j in range(len(matrixB[0])):
			# iterate through rows of Y
			for k in range(len(matrixB)):
				result[i][j] += matrixA[i][k] * matrixB[k][j]
	return result

def write(listofmatrix,filename):
	f=open(filename+'.txt','w')
	json.dump(listofmatrix,f)
	f.close()