#Luas Permukaan Bangun Ruang
import math
def LPKubus(s):
    hasil= 6 * (s * s)
    print("LP Kubus adalah ", hasil)

def LPBalok(p, l, t):
    hasil= 2 * (p*l) * (p*t) * (l*t)
    print("LP Balok adalah ", hasil)

def LPTabung(r, t):
    hasil= 2 * 3.14 * r * (r+t)
    print("LP Tabung adalah ", hasil)