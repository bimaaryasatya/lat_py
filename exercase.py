def jumlahJam(j, t):
    return j * t

def hitungGaji(jt, ta):
    return jt *  ta

nama_karyawan = str(input('Masukkan Nama: '))
jam_kerja = int(input('Masukkan Jam Kerja: '))
tarif_per_jam = float(input('Masukkan Tarif per Jam: '))
total_hari = int(input('Total Hari Kerja Sebulan: '))
jumlah_jam = jumlahJam(jam_kerja, total_hari)
jumlah_gaji = hitungGaji(jumlah_jam, tarif_per_jam)

print(f'Jumlah Gaji {nama_karyawan} per Bulan Adalah: {jumlah_gaji:,}')