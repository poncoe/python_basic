import os
import header
import json
import getpass
def akunadmin():
    z = 'ya'
    a = 0
    while z == 'ya' :
        user = input('Username = ')
        p = getpass.getpass('Password = ')
        if (user =='admin') and (p =='mimin') :
            print ('Selamat Datang',user,'Tekan Enter untuk lanjut')
            input()
            break
        elif (user =='admin') or (p =='mimin') :
            print ('Username/Password salah')
        else :
            print('Password Salah')
        a = a+1
        if a == 3 :
            print ('sudah 3x input')
            break
        print()
        z = input('Input username dan password lagi ? ya/tidak ?')
        print()
        os.system('cls')
        header.header()
        
