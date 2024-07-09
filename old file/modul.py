def jumlah(a,b):
    return a + b
def kurang(c,d):
    return c - d
def kali(e,f):
    return e * f
def bagi(g,h):
    return g / h
def tampilan():
    print("1. Penjumlahan","\n2. Pengurangan","\n3. Perkalian","\n4. Pembagian")
def operasi():
    while True:
        pilihan, a, b = int(input('Masukkan Pilihan: ')), int(input('Masukkan Bilangan Pertama=')), int(input('Masukkan Bilangan kedua=')) 
        if pilihan == 1:    
            print(a,'+',b,'=',jumlah(a,b))
        elif pilihan == 2:
            print(a,'-',b,'=',kurang(a,b))
        elif pilihan == 3:
            print(a,'x',b,'=',kali(a,b))
        elif pilihan == 4:
            print(a,'/',b,'=',bagi(a,b))
        else:
            print('Pilihan Tidak Valid')
        break