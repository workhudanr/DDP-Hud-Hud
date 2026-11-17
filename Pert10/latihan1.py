#Soal 1
import fungsilat1

print()
print("---gunakan Modul---")
fungsilat1.tambah(5,2)
fungsilat1.kurang(10,3)
fungsilat1.kali(5,6)

print()
print("---Gunakan Modul sebagai Alias---")
import fungsilat1 as f1
f1.bagi(20,2)
f1.pangkat(2,3)

print()
print("---Gunakan modul dgn memanggil sebagian fungsinya---")
from fungsilat1 import tambah,kurang
tambah(20,30)
kurang(2,3)

print()
print("Gunakan modul dgn memanggil seluruh fungsinya")
from fungsilat1 import *
tambah(20,30)
kurang(2,3)
kali(5,6)
bagi(20,2)
pangkat(2,3)

print()
print("---Gunakan Modul dgn memanggil sebagian fungsinya dengan alias---")
from fungsilat1 import tambah as add, kali as x, kurang as m
add(3,7)
x(10,10)
m(10,5)