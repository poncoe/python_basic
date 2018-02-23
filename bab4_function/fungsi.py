def perkalian(a,b,c):
	hasil = a*b*c
	return hasil

def pertambahan(a,b,c=None, d=None):
	hasil = a +b
	if c:
		hasil += c
	if d:
		hasil += 100*d
	return hasil

def pertambahan_koleksi(koleksi):
	hasil = sum(koleksi)
	return hasil

def ganti(mutable):
	if len(mutable) > 0:
		mutable[0] = 'ini udah ganti'

def ganti_im(im):
	im = 12

def bintang_satu(*args):
	print(args)

def bintang_dua(**kwargs):
	print(kwargs)

if __name__ == '__main__':
	kali = perkalian(1,2,3)
	print(kali)
	tambah = pertambahan(1,2,c=9,d=2)
	print(tambah)
	koleksi = pertambahan_koleksi([1,2,3,4,5])
	print(koleksi)
	tes = [1,2,3]
	ganti(tes)
	print(tes)
	a = 25
	ganti_im(a)
	print(a)
	bintang_satu(1,2,3,4)
	bintang_dua(h=1,b=2,c=4)
