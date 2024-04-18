warna = ['Merah', 'Kuning', 'Biru', 'Hijau']
number = [1,2,3,4,5]
desc = 'lorem ipsum dolor sit amet'
data = {'Nama':'Bima Sunu Aryasatya','NIM':23090043}

#for color in warna:
#    print(color)
#
#for deskrip in desc:
#    print(deskrip)

#for index, deskrip in enumerate (desc):
#    print(index, deskrip)

#for angka, color in zip(number, warna):
#    print(angka,color)

#for label, value in data.items():
#    print(label,":",value)

#for i in range(20): print(i, "Bilangan Genap") if i % 2 == 0 else print(i,'Bilangan Ganjil')

#i = 1
#while i <= 10:
#    print('Berhitung:',i)
#    i+=1

total_perulangan=0
while True:
    main=input('Lanjut? Ya/Tidak?: ').lower()
    if main == 'tidak':
        break
    total_perulangan += 1
print('Total Pengurangan:',total_perulangan)

i=0
while i <=20:
    if i == 10:
        i += 1
        continue
    print(i)
    i +=1