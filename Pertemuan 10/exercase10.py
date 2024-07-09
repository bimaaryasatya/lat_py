history = []
redo = []
stack = []
def undo():
    if len(history) == 0:
        print("Tidak ada yang bisa di undo")
        return
    rec = history[-1]
    if rec[0] == "+":
        history.pop()
        stack.pop()
        redo.append(f"-{rec[1:]}")
        print(f'Berhasil mengundo menambahkan "{rec[1:]}"')
    elif rec[0] == "-":
        history.pop()
        stack.append(rec[1:])
        redo.append(f"+{rec[1:]}")
        print(f'Berhasil mengundo menghapus "{rec[1:]}"')

def redoe():
    if len(redo) == 0:
        print("Tidak ada yang bisa di redo")
        return
    rec = redo[-1]
    if rec[0] == "+":
        redo.pop()
        stack.pop()
        history.append(f"-{rec[1:]}")
        print(f'Berhasil mengredo, "{rec[1:]}" telah di hapus kembali')
    elif rec[0] == "-":
        redo.pop()
        stack.append(rec[1:])
        history.append(f"+{rec[1:]}")
        print(f'Berhasil mengredo, "{rec[1:]}" telah di tambahkan kembali')

while True:
    print(f"Riwayat pencarian saat ini : {stack} \nHistori: {history} \nRedo: {redo}","\nPilihan:","\n1. Tambah Pencarian","\n2. Hapus pencarian terakhir","\n3. Undo","\n4. Redo","\n5. Keluar\n")
    inp = str(input("Pilih Operasi (1/2/3/4): "))
    if inp == "1":
        kk = input("Masukkan kata kunci pencarian: ")
        stack.append(kk)
        history.append(f"+{kk}")
        print(f'"{kk}" ditambahkan ke riwayat pencarian')
        redo.clear()
    elif inp == "2":
        print(f'"{stack[-1]}" berhasil di hapus')
        history.append(f"-{stack[-1]}")
        stack.pop()
        redo.clear()
    elif inp == "3":
        undo()
    elif inp == "4":
        redoe()
    elif inp == "5":
        break
    else:
        print("Pilihan Tidak Valid")
    print("\n")