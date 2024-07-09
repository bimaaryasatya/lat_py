import random

a = random.randint(1,10)
p = 0
while True:
    t = int(input('Tebak Angka:'))
    p += 1
    if t > a:
        print('Terlalu tinggi, turunkan')
    elif t < a:
        print('Terlalu rendah, naikkan')
    else:
        print('Tebakkan Anda Benar')
    print('Anda Telah Mencoba Sebanyak:',p)