def tampilan():
    print("Program Minghitung Kategori BMI","\nBMI < 18.5 = Kekurangan Berat Badan\n","\nBMI <= 24.9 = Berat Badan Normal","BMI < 29 atau > 25 = Kelebihan Berat Badan\n", "BMI >= 30 = Obesitas\n")

def hitung_bmi():
    
    while True:
            tinggi_badan = float(input("Masukkan Tinggi Badan dalam Kg: "))
            berat_badan = float(input("Masukkan Berat Badan dalam kg: "))
            bmi = berat_badan / (tinggi_badan ** 2)
            if bmi < 18.5:
                print(f"Tinggi Badan = {tinggi_badan}\n, "f"Berat Badan = {berat_badan}\n", f"BMI: {bmi}", f"Kategori BMI = Berat Badan Kurang")
            elif bmi <= 24.9:
                print(f"Tinggi Badan = {tinggi_badan}\n, "f"Berat Badan = {berat_badan}\n", f"BMI: {bmi}", f"Kategori BMI = Berat Badan Normal")
            elif bmi < 29.9 or bmi > 25:
                print(f"Tinggi Badan = {tinggi_badan}\n, "f"Berat Badan = {berat_badan}\n", f"BMI: {bmi}", f"Kategori BMI = Kelebihan Berat Badan")
            elif bmi >= 30:
                print(f"Tinggi Badan = {tinggi_badan}\n, "f"Berat Badan = {berat_badan}\n", f"BMI: {bmi}", f"Kategori BMI = Obesitas")
            else:
                 print("Tidak Valid")
            break