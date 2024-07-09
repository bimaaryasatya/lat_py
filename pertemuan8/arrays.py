import array as arr
import numpy as np

nilai_siswa = [90,80,70,60,50]
index = 4
print(nilai_siswa[index])

nilai_siswa.append(80)
print(nilai_siswa)

nilai_siswa[0] = 70

nilai_siswa.pop(2)
print(nilai_siswa)

print(len(nilai_siswa))
print(sum(nilai_siswa))

rata = sum(nilai_siswa) / len(nilai_siswa)
print(max(nilai_siswa))
print(min(nilai_siswa))
print(rata)

ab_avg = sum(True for i in nilai_siswa if i > rata)
print(ab_avg)