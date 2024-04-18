nama = input('Masukkan Nama: ').title()
jabatan = input('Masukkan Jabatan [Design/Programmer/Resource]: ').capitalize()
status = input('Masukkan Status Perkawinan: ').upper()

if jabatan == 'Design':
    gajipokok = 5000000
elif jabatan == 'Programmer':
    gajipokok = 10000000
elif jabatan == 'Resource':
    gajipokok == 5000000
else:
    print('Error')
    exit()

if status == "Y":
    tunjangan = 0.2 * gajipokok
else:
    tunjangan = 0

gajikotor = gajipokok + tunjangan
pajak = 0.1 * gajikotor
total = gajikotor - pajak

print("Nama: ", nama, "Jabatan: ", jabatan, f"Gaji Pokok: {gajipokok:,.2f}" f"Tunjangan Keluarga: {tunjangan:,.2f}", f"Gaji Kotor: {gajikotor:,.2f}", f"Pajak: {pajak:,.2f}", f"Total Pendapatan: {total:,.2f}")
