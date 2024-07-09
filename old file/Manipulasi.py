#string1 = "Hello"
#string2 = "World"
#int1 = 5

#print(string1 + " " + string2)
#print((string1 + " " + string2) * 9)
#print(string1 + " " + str(int1))

#list_string = ['Aku', 'Adalah', 'Saya']
#kalimat = " ".join(list_string)
#print(kalimat)

#list_kalimat = 'Ini, Adalah Sebuah Kalimat'
#kata = list_kalimat.split(', ')
#print(kata)

#kata2 = list_kalimat.replace('Kalimat', 'Kata')
#print(kata2)

#nama = 'bima aryasatya'
#nama2 = 'BIMA ARYASATYA'
#print(nama.upper())
#print(nama2.lower())
#print(nama2.capitalize())
#print(nama2.title())

#uang = 271000000000000
#print('{:,.2f}'.format(uang))
#print(f'Rp.{uang:,.2f}')

#penilaian = input('Masukkan Penilaian [Bagus/Tidak] : ').title()
#print(penilaian)

#if penilaian == 'Bagus':
    #print('Joss Gandos')
#else:
    #if penilaian == 'Tidak':
        #print('Jelek')
    #else:
        #print('invalid')

#nilai = int(input('Masukkan Nilai [0-100] : '))
#if nilai < 0 or nilai > 100:
#    print("Error: Range 0-100")
#    exit()
#else:
#    print('Benar')

#nilai = 66
#if nilai > 80:
#    print('A')
#elif nilai > 65:
#    print("B")
#elif nilai > 40:
#    print("C")
#else:
#    print('Cok Niat Sekolah Po ra?')

umur = int(input("Masukkan Umur : "))
if umur == 17:
    undangan = input('Punya Undangan [Y/T] : ')
    if undangan == "Y":
        print('Boleh Mencoblos')
    else:
        print("Minta Undangan Hey")
else:
    print("Belum Boleh Mencoblos (Masih Bocil Awokwowk)")