nama = str(input("Masukkan Nama: "))
umur = int(input("Masukkan Umur: "))
pekerjaan_ortu = str(input('Masukkan Pekerjaan Orang Tua: '))
gaji_ortu = int(input('Gaji Orang Tua: '))
ipk = float(input('IPK: '))

list_pekerjaan = ['ASN,' 'PNS', 'Pegawai Swasta', 'Petani']

if pekerjaan_ortu not in list_pekerjaan and gaji_ortu <= 1000000 and ipk >= 2.7 and umur < 25:
    print('Nama :', nama)
    print('Umur :', umur)
    print('Pekerjaan Orang Tua :', pekerjaan_ortu)
    print('Gaji Orang Tua :', gaji_ortu)
    print('IPK :', ipk)
    print('Anda Memenuhi Syarat Menerima Beasiswa')
else:
    print('Nama :', nama)
    print('Umur :', umur)
    print('Pekerjaan Orang Tua :', pekerjaan_ortu)
    print('Gaji Orang Tua :', gaji_ortu)
    print('IPK :', ipk)
    print('Anda Tidak Memenuhi Syarat Beasiswa')




