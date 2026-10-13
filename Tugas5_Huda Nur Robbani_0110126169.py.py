kendaraan = ["HagiaSophia", "Mobil", "1200cc", "Hitam", "Roda empat"]
kendaraan.append("100.000.000")
kendaraan.append("Mobil keluarga")
kendaraan.insert(1, "BMW")
print(kendaraan)    

print("=== Alat menghitung Luas Bangun Datar ===")
print("1. menghitung luas Persegi")
print("2. menghitung luas lingkaran")
print("3. menghitung luas Segitiga")

pilihan = input("Masukkan pilihan anda (1/2/3): ")

match pilihan:
    case "1":
        s = int(input("Masukkan sisi: "))
        luas = s * s
        print("Luas Persegi:", luas)
    case "2":
        PI = 3.14
        r = int(input( "masukan jari-jari: "))
        luas = PI * r * r
        print("luas lingkaran:", luas)
    case "3":
        a = int(input("masukan alas:"))
        t = int(input("masukan tinggi:"))
        luas = a * t / 2
        print("luas segitiga:", luas)
    