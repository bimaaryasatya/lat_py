list = []

def tambah_barang():
    nama = input('Masukkan Nama Barang: ')
    stok = int(input('Masukkan Jumlah Barang: '))
    list.append({"Nama Barang:", nama,"Stok:",stok})
    
    for i in list:
        print("Nama:",['nama'],"Stok")

def lihat_barang():
    for i in list:
        print(f"Nama:{i['nama']}\nStok:{i['stok']}")


