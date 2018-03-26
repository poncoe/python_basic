# read the file and return the data
def Baca():
	file = open('kalimat.txt','r')
	return file.read()
	file.close()