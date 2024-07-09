import numpy as np
import module as ex7

arr = []
siswa = int(input('Masukkan Jumlah Siswa: '))

for i in range(siswa):
    arr.append(float(input(f'\033[94mNilai Siswa ke- {i+1} :')))

print(f'\033[91mNilai Rata-Rata Semua Siswa: {ex7.avgr(arr)}')
print(f'\033[96mJumlah Siswa Dengan Nilai di Atas Rata-Rata{ex7.ab_avg(arr)}')
print(f'\033[92mSiswa Dengan Nilai Tertinggi : {ex7.max_nilai(arr)}')
print(f'\033[95mSiswa Dengan Nilai Terendah : {ex7.min_nilai(arr)}')