print("program Menghitung luas permukaan dan volume balok")

# Atur nilai variabel

panjang = float(input("masukan nilai panjang ="))
lebar = float(input("masukan nilai lebar ="))
tinggi = float(input("masukan nilai tinggi ="))

# Menghitung luas permukaan balok
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Menghitung volume balok
volume = panjang * lebar * tinggi

# Output hasil perhitungan
print("-----hasil perhitungan-----")
print(f"luas permukaan balok adalah: {luas_permukaan}")
print(f"volume balok: {volume}")
