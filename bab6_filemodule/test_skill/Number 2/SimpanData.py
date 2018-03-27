# saving data based by parameter 'L' as a list and 'nama' as a file name
import json
def Simpan(L,nama):
	with open(nama+'.txt','w') as file:
		json.dump(L,file)