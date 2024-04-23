tahun = int(input("Masukkan Tahun:"))
print(f'{tahun} Adalah Tahun Kabisat') if tahun % 4 == 0 or tahun % 100 == 0 or tahun % 400 == 0 else print(f'{tahun} Bukan Tahun Kabisat')