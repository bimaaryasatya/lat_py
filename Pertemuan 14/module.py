class Book:
    def __init__(self, judul, penulis, tahun_terbit):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit

    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_tahun(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit
    
    def get_information(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Tahun Terbit: {self.__tahun_terbit}"
    
class EBook(Book):
    def __init__(self, judul, penulis, tahun_terbit, ukuran_file):
        super().__init__(judul, penulis, tahun_terbit)
        self.__ukuran_file = ukuran_file
    
    def get_information(self):
        return f"{super().get_information()}, Ukuran: {self.__ukuran_file}"
    
    def get_book(self):
        return super()