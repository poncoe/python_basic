# count appearance of 'ar'
def Hitung(kalimat):
	ar=0
	for x in range(len(kalimat)):
		if kalimat[x]=='a' and kalimat[x+1]=='r':
			ar+=1
	return ar
