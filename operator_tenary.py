#Tenary
nilai = 75
hasil = 'A' if nilai > 75 else 'B'
print(hasil)

if nilai > 75:
    print('A')
else:
    print('B')

# operator logika
a=True
b=False
print('A AND B:',a and b)
print('A OR B:',a or b)
print('NOT A:',not a)
print('NOT B:',not b)

bayar_kuliah = bool(input('apakah sudah bayar:'))
absensi = int(input('absensi :'))

if not bayar_kuliah == False and not absensi < 70:
    print(100*'-','Hasil',100*'-')
    print('Boleh Mengikuti Ujian')
else:
    print('Tidak Diperbolehkan Mengikuti Ujian')