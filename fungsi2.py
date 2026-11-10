def celcius_ke_fahrenheit(celcius):
    Hasil=(celcius * (9/5))+ 32
    print(Hasil)



celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

#soal 2

print()

def is_genap(bilangan):
    print(bilangan % 2 == 0)

is_genap(4)
is_genap(7)

#soal 3

print()

def nilai(skor):
    if skor >= 80:
        print("lulus")
    elif skor <= 60:
        print("tidak lulus")
    else:
        print("nilai tidak valid")

nilai(30)
nilai(90)
nilai(70)

#soal 4
print()

def bilangan_ganjil(angka):
    for i in range (1, angka+1):
        if i % 2 != 0:
            print(i, end="")

bilangan_ganjil(20)