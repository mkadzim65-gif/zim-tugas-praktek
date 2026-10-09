import math

# Input dua sisi siku-siku
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

# Rumus Pythagoras: c = akar(a^2 + b^2)
sisi_miring = math.sqrt(sisi_a**2 + sisi_b**2)

print(f"Panjang sisi miring (hipotenusa) adalah: {sisi_miring:.2f}")