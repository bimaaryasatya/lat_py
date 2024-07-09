from queue import LifoQueue as lq

# Inisialisasi objek stack
stack = lq(maxsize=5)

# Menambahkan elemen stack
stack.put('Wahyu')
stack.put('Wildan')
stack.put('Abdul')
stack.put('Saif')
stack.put('Dimas')

# Panggil stack
print(stack.queue)

# Panggil stack
stack.get()
print(stack.queue)

# Menampilkan Nilai Top
print(stack.queue[-1])

# Mengecek stack kosong atau tidak (True/False)
print(stack.empty())

# Mengecek stack full atau tidak (True/False)
print(stack.full())