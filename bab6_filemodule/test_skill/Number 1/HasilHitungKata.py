# write the result into a new file
def Tulis(ar):
	write = open('result.txt','w')
	write.write('Sum of "ar": '+str(ar))
	write.close()