import json

def cekSaldo():
	file = open('saldo.txt','r')
	return json.load(file)

def tarikTunai():
	saldo = cekSaldo()
	tarik = int(input('Masukkan Nominal Transaksi: '))
	if saldo-tarik >= 0:
		saveto = open('saldo.txt','w')
		json.dump(saldo-tarik, saveto)
	else:
		print('Penarikan Anda Terlalu Besar, Saldo Tidak Mencukupi!')

def setorTunai():
	saldo = cekSaldo()
	setor = int(input('Masukkan Nominal Transaksi: '))
	if setor >= 0:
		save = open('saldo.txt','w')
		json.dump(saldo+setor, save)
	else:
		print('Setor Tunai Tidak Boleh Negatif!')

if __name__ == '__main__':
	print('Saldo: Rp%s' %cekSaldo())
	print('1. Tarik Tunai\n'+'2. Setor Tunai\n')
	pilihan=input('Masukkan Pilihan: ')

	if pilihan=='1':
		tarikTunai()
	elif pilihan=='2':
		setorTunai()
	else:
		print('Pilihan anda tidak valid, silakan mengulang program lagi')