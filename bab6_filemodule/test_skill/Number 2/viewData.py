# print out from parameter b
def viewAll(b):
	print("NIM\tNama\tNilai UTS")
	# Lanjutkan di bawah
	for x in range(len(b)):
		print('%s\t%s\t%s' %(b[x][0],b[x][1],b[x][2]))