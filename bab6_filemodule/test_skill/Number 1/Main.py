import BacaDataTxt
import PrintKalimat
import HitungKata
import PrintHitungKata
import HasilHitungKata

if __name__ == '__main__':
	# Call the module, so this program can be run
	# Don't ever try to use 'print()' syntax here

	read_file=BacaDataTxt.Baca()
	PrintKalimat.Cetak(read_file)
	count_ar=HitungKata.Hitung(read_file)
	PrintHitungKata.Cetak(count_ar)
	HasilHitungKata.Tulis(count_ar)