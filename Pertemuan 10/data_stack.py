data_stack = []

data_stack.append('Abdul')
data_stack.append('Subandrio')
data_stack.append('Wildan')
data_stack.append('Wahyu')
data_stack.append('Asep')

print(data_stack)

# Hapus Elemen data terakhir
data_stack.pop()
print(data_stack)

# Melihat Nilai Top/Peek
print(f'Nilai Peek/Top: {data_stack[-1]}')

# Melihat Apakah stack kosong atau tidak
print('Apakah List Kosong?:','Ya' if len(data_stack) == 0 else 'Tidak')

# Melihat Jumlah Data Stack
print(len(data_stack))

