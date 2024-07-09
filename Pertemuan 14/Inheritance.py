# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def get_name(self):
#         print(self.name)
    
#     def meowing(self):
#         print(self.sound)

# class car(Animal):
#     def __init__(self, name, brand, sound):
#         super().__init__(name, sound)
#         self.brand = brand

# car1 = car("Supra", "Toyota", "Vroom")
# car1.meowing()

class Manusia:
    def __init__(self, InputHidung, InputMata, InputRambut):
        self.hidung = InputHidung
        self.mata = InputMata
        self.rambut = InputRambut
    
class Pacar:
    def __init__(self, nama):
        self.nama = nama

    def get_pacar(self):
        return f'Pacar: {self.nama}'

class Wildan(Manusia,Pacar):
    def __init__(self,hidung,mata,rambut,kulit,nama):
        Manusia.__init__(self, hidung,mata,rambut)
        Pacar.__init__(self, nama)
        self.kulit = kulit

    def information(self):
        return f'''Hidung: {self.hidung}\nKulit: {self.kulit}
        Rambut: {self.rambut}\nKulit: {self.kulit}\nNama Pacar: {self.nama}'''
    
wildan = Wildan('Pesek','Sipit','Mulet','India','Sapto')
print(wildan.information())
# print(wildan.get_kulit())
# print(wildan.get_pacar())