print("Program menghitung luas permukaan dan volume kerucut")
# Atur nilai variabel
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))
garis_pelukis = float(input("Masukan panjang garis pelukis: "))
PHI = 3.14
# Menghitung luas selimut kerucut
luas_selimut = PHI * jari_jari * garis_pelukis 

# Menghitung luas permukaan kerucut
luas_permukaan = luas_selimut + (PHI * jari_jari**2)

# Menghitung volume kerucut
volume = PHI * jari_jari**2 * tinggi / 3

# Output hasil perhitungan 
print("---Hasil perhitungan----")
print(f"Luas permukaan kerucut adalah: {luas_permukaan}")
print(f"Volume kerucut adalah: {volume}")
