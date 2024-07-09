# class kar:
#     def __init__(self, merk, pabrik, tahun):
#         self.merk = merk
#         self.pabrik = pabrik
#         self.tahun = tahun

# kar1 = kar('499P','Ferrari','2023')
# print(kar1.__dict__)

# kar2 = kar('919','Porsche','2017')
# print(kar2.__dict__)

class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def get_luas(self) -> int:
        return self.panjang * self.lebar
    
    def set_panjang(self, panjang):
        self.panjang = panjang
        return self

    def set_lebar(self, lebar):
        self.lebar = lebar
        return self

persegi = PersegiPanjang(12,15)
print(persegi.get_luas())

persegi.set_panjang(20).set_lebar(16)
print(persegi.get_luas())